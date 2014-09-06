from .utils import SESSION_KEY_CURRENT_OS
from .forms import OSForm


class CurrentOSMixin(object):

    allowed_oses = OSForm.OS_CHOICES

    def get_context_data(self, **kwargs):
        """Inject current active OS key and the choice form into context.
        """
        # Zip the 2-tuple into a [keys, values] generator, and use next() to
        # get its first item (i.e. keys).
        allowed_os_keys = next(zip(*self.allowed_oses))

        os = self.request.session.get(SESSION_KEY_CURRENT_OS)
        if os not in allowed_os_keys:
            os = OSForm.OS_CHOICES[0][0]
        os_form = OSForm(initial={'os': os})
        kwargs.update({'current_os': os, 'os_form': os_form})
        return super().get_context_data(**kwargs)
