from .models import Reger
from django.forms import ModelForm, EmailInput, TextInput

class RegerForm(ModelForm):
    class Meta:
        model = Reger
        fields = ['email', 'password']

        widgets = {
            "email": EmailInput(attrs={
                'type': 'email',
                'class': 'register-input',
                'placeholder': 'Email address'
            }),
            "password": TextInput(attrs={
                'type': 'password',
                'class': 'register-input',
                'placeholder': 'Password'
            })
        }
