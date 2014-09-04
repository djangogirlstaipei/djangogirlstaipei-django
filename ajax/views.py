from django.http import JsonResponse
from django.views.generic.edit import BaseFormView
from base.utils import SESSION_KEY_CURRENT_OS
from base.forms import OSForm


class SetOSView(BaseFormView):

    form_class = OSForm

    def form_invalid(self, form):
        return self.render_to_response({'errors': form.errors}, status=400)

    def form_valid(self, form):
        os = form.cleaned_data['os']
        self.request.session[SESSION_KEY_CURRENT_OS] = os
        return self.render_to_response({'current_os': os})

    def render_to_response(self, context, **kwargs):
        context.pop('form', None)   # From FormMixin.
        context.pop('view', None)   # From ContextMixin.
        return JsonResponse(context, **kwargs)
