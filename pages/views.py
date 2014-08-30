import os
from django.http import Http404
from django.views.generic import TemplateView
from .utils import markdown_to_html


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class TutorialListView(TemplateView):
    template_name = 'pages/tutorial_list.html'


class MarkdownPageView(TemplateView):

    template_name = 'pages/page.html'

    def get_content(self, style):
        """Get content to display in the page.

        :param str style: Name of Pygment style to use for syntax highlighting.
            If an invalid name is provided, the default style is used.
        """
        dirname = os.path.dirname(__file__)
        filename = '{path}.md'.format(path=self.kwargs['path'])
        path = os.path.join(dirname, 'pages', filename)
        try:
            with open(path) as f:
                markdown = f.read()
        except OSError:
            raise Http404
        html, meta, hilite_style = markdown_to_html(markdown, style)
        return html, meta, hilite_style

    def get_context_data(self, **kwargs):
        style = self.request.GET.get('style', 'friendly')
        content, meta, hilite_style = self.get_content(style)
        kwargs.update({
            'content': content,
            'title': meta.get('title', ''),
            'hilite_style': hilite_style,
        })
        return super().get_context_data(**kwargs)
