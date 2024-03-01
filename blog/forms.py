from django import forms
from .models import Post

class PostForm(forms.ModelForm): # ModelForm is a Django helper
    class Meta: # This is where we define which model the form is going to be based on
        model = Post
        fields = ('title', 'abstract', 'text',)