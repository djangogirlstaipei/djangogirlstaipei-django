import os
from django.http import Http404
from django.views.generic import TemplateView, RedirectView
from .utils import markdown_to_html


# class HomeView(TemplateView):
#     template_name = 'pages/home.html'


# class TutorialListView(TemplateView):
#     template_name = 'pages/tutorial_list.html'


class HomeView(RedirectView):
    permanent = False
    url = 'http://djangogirls.org/taipei'


class TutorialListView(RedirectView):
    permanent = False
    url = 'http://djangogirls.org/taipei'


class MarkdownPageView(TemplateView):

    template_name = 'pages/page.html'

    def get_content(self, style):
        """Get content to display in the page.

        :param str style: Name of Pygment style to use for syntax highlighting.
            If an invalid name is provided, the default style is used.
        """
        path = self.kwargs['path']
        dirname = os.path.dirname(__file__)
        filename = '{path}.md'.format(path=path)
        abspath = os.path.join(dirname, 'pages', filename)
        try:
            with open(abspath) as f:
                markdown = f.read()
        except OSError:
            raise Http404
        html, meta, hilite_style = markdown_to_html(markdown, path, style)
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
