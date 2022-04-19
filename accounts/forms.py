from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    
    password = forms.CharField( widget=forms.PasswordInput(attrs={
        'class': 'input100',
        
    }), min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100',
    }))

    class Meta:
        model = Account
        fields = ('full_name', 'email', 'password', 'contact')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                'Password did not match'
            )

    def __init__(self, *args, **kargs):
        super(RegistrationForm, self).__init__(*args, **kargs)
        self.fields['full_name'].widget.attrs.update({'class': 'input100'})
        self.fields['email'].widget.attrs.update({'class': 'input100'})
        self.fields['contact'].widget.attrs.update({'class': 'input100'})
