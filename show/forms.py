from django import forms
from models import Show
from globals.constants import PLENGTH, ILENGTH

PTYPE = (
         (0, u'Dictionary'),
         (1, u'Increase'),
         (2, u'Decrease'),
         (3, u'Switch'))

class showForm(forms.ModelForm):
    length = forms.IntegerField()
    type = forms.ChoiceField(widget = forms.RadioSelect, choices = PTYPE)
    
    class Meta:
        model = Show
        fields = ('length', 'type')
        
class piForm(forms.Form):
    
    def set__(self, p ,i ):
        self.fields['permutation'] = p
        self.fields['index'] = i
        
    permutation = forms.CharField(max_length = PLENGTH)
    index = forms.CharField(max_length = ILENGTH)