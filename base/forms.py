from django import forms


class OSForm(forms.Form):
    os = forms.CharField()
