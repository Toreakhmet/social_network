from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('profile_image',)

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['content', 'images', 'video']
