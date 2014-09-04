from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^os/$', views.SetOSView.as_view(), name='set_os'),
)
