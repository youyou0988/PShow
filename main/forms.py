from django import forms
from globals.constants import NAMELENGTH, DIRLENGTH, IDLENGTH, PWDLENGTH

class RegisterForm(forms.Form):
    sid = forms.CharField(max_length = IDLENGTH)
    name = forms.CharField(max_length = NAMELENGTH)
    pwd = forms.CharField(max_length = PWDLENGTH, widget = forms.widgets.PasswordInput)
    pwdc = forms.CharField(max_length = PWDLENGTH, widget = forms.widgets.PasswordInput)

class LoginForm(forms.Form):
    sid = forms.CharField(max_length = IDLENGTH)
    pwd = forms.CharField(max_length = PWDLENGTH, widget = forms.widgets.PasswordInput)
