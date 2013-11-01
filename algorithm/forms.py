from django import forms
from globals.constants import NAMELENGTH

class addForm(forms.Form): 
    name = forms.CharField(max_length = NAMELENGTH)
    source = forms.FileField(required = False)
    
class updateForm(forms.Form):
    source = forms.FileField(required = False)