from .utils import SESSION_KEY_CURRENT_OS
from .forms import OSForm


class CurrentOSMixin(object):

    allowed_oses = (
        ('windows', 'Windows'),
        ('osx', 'OS X'),
        ('linux', 'Linux'),
    )

    def get_context_data(self, **kwargs):
        os = self.request.session.get(SESSION_KEY_CURRENT_OS)
        if os not in dict(self.allowed_oses).keys():
            os = 'windows'
        os_form = OSForm(initial={'os': os})
        kwargs.update({'current_os': os, 'os_form': os_form})
        return super().get_context_data(**kwargs)
