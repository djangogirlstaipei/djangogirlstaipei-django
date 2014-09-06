from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import View

SESSION_KEY_CURRENT_OS = 'current_os'


class AjaxViewJSONEncoder(DjangoJSONEncoder):

    def default(self, o):
        if isinstance(o, View):
            try:
                request = o.request
            except AttributeError:
                return None
            return request.build_absolute_uri()
        return super().default(o)
