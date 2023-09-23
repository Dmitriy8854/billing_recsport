from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from .models import User


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        fields = ("first_name", "last_name", "username", "email")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
