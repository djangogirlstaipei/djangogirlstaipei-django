from django.template import Library
from django.contrib.staticfiles.storage import staticfiles_storage

register = Library()


@register.simple_tag(takes_context=True)
def absolute_static(context, path):
    url = staticfiles_storage.url(path)
    try:
        request = context['request']
    except KeyError:
        return ''
    return request.build_absolute_uri(url)
