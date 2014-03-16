from django import forms
from django.contrib.auth.models import User

from gofish.models import Player

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class PlayerForm(forms.ModelForm):
    ranking = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    money = forms.IntegerField(widget=forms.HiddenInput(), initial=500)
    
    class Meta:
        model = Player
        fields = ('ranking', 'money')
