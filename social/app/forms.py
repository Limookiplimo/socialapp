from django.forms import ModelForm
from .models import Post
from django import forms

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url','body']
        labels = {
            'body': 'Caption'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows':3,'placeholder':'Caption your post...','class': 'font1 text-4xl'}),
            'url': forms.TextInput(attrs={'placeholder':'Paste url...'})
        }


class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows':3,'class': 'font1 text-4xl'}),
        }


