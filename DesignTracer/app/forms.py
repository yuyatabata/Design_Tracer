from django import forms
from django.forms import ModelForm
from .models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'theme', 'break_down', 'key_point']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '名前/タイトル'}),
            'theme': forms.Textarea(
                attrs={'placeholder': '主張の理解：テーマ、伝えたいことは？', 'rows': "1"}),
            'break_down': forms.Textarea(
                attrs={'placeholder': '分析/言語化：レイアウト・余白/配色/文字組み/あしらい', 'rows': "5"}),
            'key_point': forms.Textarea(
                attrs={'placeholder': '抽象化：外せないキーになる部分は？', 'rows': "1"}),                         
        }