from django import forms
from django.contrib.auth.models import User

from gofish.models import Player

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class PlayerForm(forms.ModelForm):
    ranking = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    money = forms.IntegerField(widget=forms.HiddenInput(), initial=100)
    
    class Meta:
        model = Player
        fields = ()