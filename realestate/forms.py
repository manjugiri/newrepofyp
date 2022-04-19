# from attr import fields
from django.core import validators
from django import forms
from .models import ApplyAgent

from .models import ApplyAgent, Properti

class addprop(forms.ModelForm):
    class Meta:
        model = Properti
        fields = '__all__'
        exclude = ['video']
        
class apply_agent(forms.ModelForm):
    class Meta:
        model = ApplyAgent
        fields = ['Agency_name', 'Agency_Location', 'Agency_Contact','Agency_Email','Agency_Description', 'Agency_logo', 'is_approved' ]
        exclude = ['is_approved','user']

    def __init__(self, *args, **kargs):
            super(apply_agent, self).__init__(*args, **kargs)
            self.fields['Agency_name'].widget.attrs.update({'class': 'input100'})
            self.fields['Agency_Location'].widget.attrs.update({'class': 'input100'})
            self.fields['Agency_Contact'].widget.attrs.update({'class': 'input100'})
            self.fields['Agency_Email'].widget.attrs.update({'class': 'input100'})
            self.fields['Agency_Description'].widget.attrs.update({'class': 'input100'})
