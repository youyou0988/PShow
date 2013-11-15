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
    
    def set__(self,p,idx,i,op,oidx,oi,num):
        self.fields['permutation'] = p
        self.fields['middle'] = idx
        self.fields['index'] = i
        self.fields['oldpermutation'] = op
        self.fields['oldmiddle'] = oidx
        self.fields['oldindex'] = oi
        self.fields['num'] = num
        
		
        
    permutation = forms.CharField(max_length = PLENGTH,label="")
    index = forms.CharField(max_length = ILENGTH,label="")
    middle = forms.CharField(max_length = PLENGTH,label="")
    oldindex = forms.CharField(max_length = PLENGTH,label="")
    oldmiddle = forms.CharField(max_length = PLENGTH,label="")
    oldpermutation = forms.CharField(max_length = PLENGTH,label="")
    num = forms.CharField(max_length = PLENGTH,label="")
