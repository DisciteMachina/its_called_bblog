# blog/forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date']  # Include the fields for your Post model
        exclude = ['published_date']