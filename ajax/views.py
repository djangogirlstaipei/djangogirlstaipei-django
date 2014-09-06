from django.http import JsonResponse
from django.views.generic import FormView
from base.utils import SESSION_KEY_CURRENT_OS, AjaxViewJSONEncoder
from base.forms import OSForm


class AjaxFormView(FormView):
    """Ajax-ized form view that returns a response of given type.

    The default implementation returns a JSON response, and only allows POST,
    returning 405 NOT ALLOWED for all other requests.
    """

    http_method_names = ['post']
    response_class = JsonResponse
    encoder = AjaxViewJSONEncoder

    def form_valid(self, form):
        context_data = self.get_context_data(data=form.cleaned_data)
        return self.render_to_response(context_data)

    def form_invalid(self, form):
        context_data = self.get_context_data(errors=form.errors)
        return self.render_to_response(context_data, status=400)

    def render_to_response(self, data, **response_kwargs):
        """Overrides TemplateResponseMixin to provide a JSON response instead.
        """
        klass = self.response_class
        return klass(data=data, encoder=self.encoder, **response_kwargs)


class SetOSView(AjaxFormView):

    form_class = OSForm

    def form_valid(self, form):
        os = form.cleaned_data['os']
        self.request.session[SESSION_KEY_CURRENT_OS] = os
        return super().form_valid(form)
