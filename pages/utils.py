import os
import copy
import collections
import json
import re
import mistune
import yaml
from pygments import highlight
from pygments.util import ClassNotFound
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from slugify import slugify
from django.conf import settings
from django.contrib.staticfiles import finders


FRONT_MATTER_PATTERN = re.compile(r'^---\n(.*?\n)---', re.DOTALL)


class BlockGrammar(mistune.BlockGrammar):

    # Fix trailing newline bug in Mistune.
    block_code = re.compile(r'^( {4}[^\n]+\n)+')

    os_switch = re.compile(
        r'^ *\({3} *([\w _-]+) *\n'     # ((( class names
        r'([\s\S]+?)\s*'
        r'\){3} *(?:\n+|$)'             # )))
    )


class BlockLexer(mistune.BlockLexer):

    grammar_class = BlockGrammar
    default_rules = copy.copy(mistune.BlockLexer.default_rules)
    default_rules.insert(5, 'os_switch')

    def parse_os_switch(self, m):
        self.tokens.append({
            'type': 'os_switch_open',
            'os': m.group(1),
        })
        self.parse(m.group(2))
        self.tokens.append({
            'type': 'os_switch_close',
        })


class InlineGrammar(mistune.InlineGrammar):

    # Math inline. Two dollars (not one). We don't implement block math yet.
    math = re.compile(r'^(\$+)\s*(.*?[^`])\s*\1(?!\$)')

    # Override plain text pattern to add the dollar sign as a markup char.
    text = re.compile(r'^[\s\S]+?(?=[\\<!\[_*`~\$]|https?://| {2,}\n|$)')


class InlineLexer(mistune.InlineLexer):

    grammar_class = InlineGrammar
    default_rules = copy.copy(mistune.InlineLexer.default_rules)
    default_rules.insert(8, 'math')

    def output_math(self, m):
        text = m.group(2)
        return self.renderer.inline_math(text)


class Markdown(mistune.Markdown):

    def __init__(self, renderer=None, inline=None, block=None, **kwargs):
        if block is None:
            block = BlockLexer
        if inline is None:
            inline = InlineLexer
        super().__init__(renderer, inline, block, **kwargs)

    def parse_os_switch_open(self):
        return self.renderer.os_switch_open(os=self.token['os'])

    def parse_os_switch_close(self):
        return self.renderer.os_switch_close()


class Renderer(mistune.Renderer):
    """Custom Markdown to HTML renderer.
    """
    def __init__(self, formatter, bundlepath, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bundlepath = bundlepath or ''
        self.formatter = formatter
        self.id_slugs = collections.defaultdict(lambda: 0)

    def os_switch_open(self, os):
        return '<div class="os {name}">\n'.format(name=os)

    def os_switch_close(self):
        return '</div>\n'

    def header(self, text, level, raw=None):
        """Auto header ID from slug of text.
        """
        slug = slugify(text)
        if self.id_slugs[slug]:
            slug = '{slug}-{n}'.format(slug=slug, n=self.id_slugs[slug])
        self.id_slugs[slug] += 1
        return '<h{level} id="{id}">{text}</h{level}>\n'.format(
            level=level, text=text, id=slug,
        )

    def block_code(self, code, lang):
        """Implement syntax highlighting with Pygments.
        """
        try:
            lexer = get_lexer_by_name(lang)
        except ClassNotFound:
            return super().block_code(code, lang)
        return highlight(code, lexer, self.formatter)

    def image(self, src, title, text):
        """Implement local static file resolving.
        """
        src = self._resolve_asset_path(src)
        return super().image(src, title, text)

    def inline_math(self, src):
        return '<span class="math">{src}</span>'.format(src=src)

    def _resolve_asset_path(self, path):
        if path.startswith('javascript:'):  # Taken from mistune.
            return path
        elif path.startswith('//') or '://' in path:    # Probably absolute.
            return path
        abspath = '/'.join([
            c.strip('/') for c in (
                '', settings.STATIC_URL, self.bundlepath, path,
            )
        ])
        return abspath


class TutorialRenderer(Renderer):
    """Custom Markdown to HTML renderer for tutorial pages.
    """
    CONSOLE_DELIMITER_PATTERN = re.compile(r'^---([\w-]+)$', re.MULTILINE)

    def block_code(self, code, lang):
        """Implement console language rendering.
        """
        if lang == 'console':
            return self.block_console(code)
        return super().block_code(code, lang)

    def block_console(self, content, default='default'):
        """Special OS-specific "console language"

        A console block is similar to a code block, but instead of outputting
        content verbatim, a console block can optionally use ``---(os-name)``
        delimiters to denote OS-specific commands. The first block is the
        fallback block, and its OS is specified in ``default``.
        """
        pattern = self.CONSOLE_DELIMITER_PATTERN
        matches = [b.strip() for b in pattern.split(content)]
        matches.insert(0, default)

        it = iter(matches)
        str_format = '<pre class="os {name}"><code>{code}</code></pre>'
        return '<div>{code}</div>\n'.format(code='\n'.join([
            str_format.format(name=name, code=next(it)) for name in it
        ]))

    def table(self, header, body):
        """Render table with Bootstrap .table class
        """
        str_format = (
            '<table class="table">\n<thead>{thead}</thead>\n'
            '<tbody>\n{tbody}</tbody>\n</table>\n'
        )
        return str_format.format(thead=header, tbody=body)


def markdown_to_html(path, style=None, renderer_cls=None):
    """Renders given Markdown input to HTML.

    :path str: Static file path to a given post. The "post" should be a
        directory containing file ``text.md``.
    :prefix str: Prefix prepended to :path: when resolving static file path.
        Default is ``posts``.
    :return: HTML output, front-matter meta, and CSS. If no valid front-matter
        can be found, the second item returned will be an empty ``dict``.
    :rtype: A three-tuple (``str``, ``dict``, ``str``), or ``None`` on errors.
    """
    if renderer_cls is None:
        renderer_cls = Renderer
    try:
        with open(os.path.join(finders.find(path) or '', 'text.md')) as f:
            text = f.read()
    except OSError:
        return None
    if style is None:
        style = 'default'
    try:
        formatter = HtmlFormatter(style=style)
    except ClassNotFound:
        formatter = HtmlFormatter(style='default')
    renderer = renderer_cls(formatter=formatter, bundlepath=path)
    md = Markdown(renderer=renderer)
    fm_match = FRONT_MATTER_PATTERN.match(text)
    front_matter = {}
    if fm_match:
        try:
            front_matter = yaml.load(fm_match.group(1))
        except yaml.YAMLError:
            pass
        else:
            offset = fm_match.end(0) + 1
            text = text[offset:]
    html = md.render(text)
    return html, front_matter, formatter.get_style_defs('.highlight > pre')


def get_posts_data(path):
    with open(finders.find(path)) as f:
        data = json.load(f)
    return data
