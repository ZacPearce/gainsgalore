from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_coach']

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']