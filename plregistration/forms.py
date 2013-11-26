"""
Forms and validation code for user registration.

"""
from django import forms
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationFormUniqueEmail
from captcha.fields import CaptchaField

import fields as recapthca_fields

attrs_dict = { 'class': 'required' }

class RegistrationEmail(RegistrationFormUniqueEmail):
  username = forms.RegexField(regex=r'(?u)^\w+$',
                              max_length=30,
                              widget=forms.TextInput(attrs=attrs_dict),
                              label=_("Username"),
                              error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
  captcha = recapthca_fields.ReCaptchaField()
