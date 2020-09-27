from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import Post,ContactModel
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ContactForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    
    class Meta:
        model = ContactModel
        exclude = ['time']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email Address'}),
            'message': Textarea(attrs={'placeholder': 'Message'})
        }