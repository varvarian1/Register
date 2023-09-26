from .models import Reger
from django.forms import ModelForm, EmailField, CharField

class RegerForm(ModelForm):
    class Meta:
        model = Reger
        fields = ['email', 'password']

        widgets = {
            "email": EmailField(attrs={
                'type': 'email',
                'class': 'register-input',
                'placeholder': 'Email address'
            }),
            "password": CharField(attrs={
                'type': 'password',
                'class': 'register-input',
                'placeholder': 'Password'
            })
        }
