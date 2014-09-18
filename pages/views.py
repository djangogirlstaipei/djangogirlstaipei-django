import os
from django.http import Http404
from django.views.generic import TemplateView, RedirectView
from base.views import CurrentOSMixin
from .utils import get_posts_data, markdown_to_html, TutorialRenderer


# class HomeView(TemplateView):
#     template_name = 'pages/home.html'


class HomeView(RedirectView):
    permanent = False
    url = 'http://djangogirls.org/taipei'


class TutorialListView(TemplateView):

    template_name = 'pages/tutorial_list.html'

    def get_context_data(self, **kwargs):
        data = get_posts_data(os.path.join('pages', 'posts', 'info.json'))
        kwargs['tracks'] = data['tutorials']['tracks']
        return super().get_context_data(**kwargs)


class MarkdownPageView(TemplateView):

    template_name = 'pages/page.html'
    renderer_class = None

    def get_content(self, style):
        """Get content to display in the page.

        :param str style: Name of Pygment style to use for syntax highlighting.
            If an invalid name is provided, the default style is used.
        """
        comps = os.path.join(self.kwargs['path'].split('/'))
        bundlepath = os.path.join('pages', 'posts', *comps) + '.textbundle'
        results = markdown_to_html(bundlepath, style, self.renderer_class)
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


class TutorialMarkdownPageView(CurrentOSMixin, MarkdownPageView):

    template_name = 'pages/tutorial_detail.html'
    renderer_class = TutorialRenderer

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update({'os_list': self.allowed_oses})
        return data
