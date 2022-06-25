from socket import fromshare
from django import forms
from .models import Post
from django.contrib.auth.base_user import AbstractBaseUser


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


