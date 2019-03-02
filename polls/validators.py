from django.core.exceptions import ValidationError
from django.forms import CharField
from django.core import validators

# def clean_username(self):
#     username = self.cleaned_data['username']
#     from pprint import pprint
#     pprint('testtesttest')
#     pprint(len(username))
#     if len(username) > 10:
#         raise ValidationError("username is too long.")
#     return username
