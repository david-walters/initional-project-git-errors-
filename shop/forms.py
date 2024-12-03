from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password2 = forms.CharField(widget=forms.PasswordInput(),
    label='Confirm password', help_text='')
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {
            'username': '',
        }