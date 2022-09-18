from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = (
            'title',
            'page_title',
            'content', 
            'author',          
            )
        labels = {
            'title': 'title',
            'page_title': 'page title',
            'content': 'content',         
            }

class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'page_title',
            'content',
            )
        labels = {
            'title': 'title ',
            'page_title': 'page title ',
            'content': 'content ',
            'author': 'author',
            }

