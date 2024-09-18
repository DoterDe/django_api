
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile
from django.contrib.auth.models import User


class UserForm(AuthenticationForm):
    class Meta:
        model = User
        fields =  ['username', 'password' ]


class CreatePostForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'cv', 'photo', 'id_photo']