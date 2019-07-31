from django import forms
from .models import user

class userForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'email': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
