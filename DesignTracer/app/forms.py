from django import forms
from django.forms import ModelForm
from .models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'comment']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '名前/タイトル'}),
            'comment': forms.Textarea(
                attrs={'placeholder': 'なぜかっこいいと思ったの？'}),
        }