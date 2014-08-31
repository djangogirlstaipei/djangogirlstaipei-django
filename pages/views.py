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
        comps = os.path.join(self.kwargs['path'].split('/'))
        bundlepath = os.path.join('pages', 'posts', *comps) + '.textbundle'
        results = markdown_to_html(bundlepath, style)
        if results is None:
            raise Http404
        html, meta, hilite_style = results
        return html, meta, hilite_style

    def get_context_data(self, **kwargs):
        style = self.request.GET.get('style', 'friendly')
        content, meta, hilite_style = self.get_content(style)
        kwargs.update({
            'content': content, 'meta': meta,
            'hilite_style': hilite_style,
        })
        return super().get_context_data(**kwargs)
