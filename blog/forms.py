from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import Post,ContactModel

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['time']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email Address'}),
            'message': Textarea(attrs={'placeholder': 'Message'})
        }