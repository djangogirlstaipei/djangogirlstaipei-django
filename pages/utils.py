import os
import collections
import mistune
import re
import yaml
from pygments import highlight
from pygments.util import ClassNotFound
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from slugify import slugify
from django.conf import settings


FRONT_MATTER_PATTERN = re.compile(r'^---\n(.*?\n)---', re.DOTALL)


class MarkdownRenderer(mistune.Renderer):
    """Custom Markdown to HTML renderer.
    """
    def __init__(self, formatter, asset_prefix, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.asset_prefix = asset_prefix or ''
        self.formatter = formatter
        self.id_slugs = collections.defaultdict(lambda: 0)

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
        src = self._resolve_relative_path(src)
        return super().image(src, title, text)

    def _resolve_relative_path(self, path):
        if path.startswith('javascript:'):  # Taken from mistune.
            return ''
        elif path.startswith('//') or '://' in path:    # Probably absolute.
            return path
        abspath = '/'.join([
            c.strip('/') for c in (
                '', settings.STATIC_URL, 'pages/page-assets',
                self.asset_prefix, path,
            )
        ])
        return abspath


def markdown_to_html(markdown, path, style=None):
    """Renders given Markdown input to HTML.

    :return: HTML output, front-matter meta, and CSS. If no valid front-matter
        can be found, the second item returned will be an empty ``dict``.
    :rtype: A three-tuple (``str``, ``dict``, ``str``).
    """
    if style is None:
        style = 'default'
    try:
        formatter = HtmlFormatter(style=style)
    except ClassNotFound:
        formatter = HtmlFormatter(style='default')
    renderer = MarkdownRenderer(formatter=formatter, asset_prefix=path)
    md = mistune.Markdown(renderer=renderer)
    fm_match = FRONT_MATTER_PATTERN.match(markdown)
    if fm_match:
        try:
            front_matter = yaml.load(fm_match.group(1))
        except yaml.YAMLError:
            front_matter = {}
        else:
            offset = fm_match.end(0) + 1
            markdown = markdown[offset:]
    html = md.render(markdown)
    return html, front_matter, formatter.get_style_defs('.highlight > pre')
