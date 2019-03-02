from django import forms
from . import validators

class TitleForm(forms.Form):
    username = forms.CharField(label="new title", required=True, max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from pprint import pprint
        pprint('titleform init')

    def clean(self):
        cleaned_data = super().clean()
        from pprint import pprint
        pprint('testtesttest')

        pprint(len(cleaned_data.get('username')))
        if len(cleaned_data.get('username')) > 10:
            raise forms.ValidationError("username is too long.")
        return cleaned_data
