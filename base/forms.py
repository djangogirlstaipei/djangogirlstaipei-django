from django.utils.translation import ugettext_lazy as _
from django import forms


class OSForm(forms.Form):

    WINDOWS = 'windows'
    OSX = 'osx'
    LINUX = 'linux'

    OS_CHOICES = (
        (WINDOWS, _('Windows')),
        (OSX, _('macOS')),
        (LINUX, _('Linux')),
    )

    os = forms.ChoiceField(choices=OS_CHOICES)
