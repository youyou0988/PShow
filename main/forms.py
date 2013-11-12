from django import forms
from globals.constants import NAMELENGTH, DIRLENGTH, IDLENGTH, PWDLENGTH

class RegisterForm(forms.Form):
    sid = forms.CharField(max_length = IDLENGTH,label='UserId')
    name = forms.CharField(max_length = NAMELENGTH,label='UserName')
    pwd = forms.CharField(max_length = PWDLENGTH, widget = forms.widgets.PasswordInput,label='Password')
    pwdc = forms.CharField(max_length = PWDLENGTH, widget = forms.widgets.PasswordInput,label='Confirm Password')

class LoginForm(forms.Form):
    sid = forms.CharField(max_length = IDLENGTH,label='UserId')
    pwd = forms.CharField(max_length = PWDLENGTH, widget = forms.widgets.PasswordInput,label='Password')
