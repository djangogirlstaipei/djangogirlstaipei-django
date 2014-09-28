from django.core.urlresolvers import reverse
from django.template import Library, TemplateSyntaxError


register = Library()


@register.simple_tag
def page_url(*args, **kwargs):
    if not args:
        raise TemplateSyntaxError(
            'page_url expects at least one positional argument.'
        )
    target = args[0]
    if target.startswith('//') or '://' in target:
        return target
    return reverse('pages:page', args=args, kwargs=kwargs)
