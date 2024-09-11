from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CreatePostForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'cv', 'photo', 'id_photo']