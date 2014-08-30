from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^tutorials/$', views.TutorialListView.as_view(),
        name='tutorial_list'),
    url(r'^(?P<path>[\w\/-]+)/$', views.MarkdownPageView.as_view(),
        name='page'),
)
