from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget

from .models import Post, Comment
from .models import Post  # Adjust based on your models
from taggit.forms import TagWidget 

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget(attrs={'placeholder': 'Add tags, separated by commas'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']