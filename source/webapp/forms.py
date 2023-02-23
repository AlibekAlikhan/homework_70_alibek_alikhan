from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    text = forms.CharField(max_length=3000, required=True, label="Текст", widget=widgets.Textarea)
    detail_text = forms.CharField(max_length=3000, required=True, label="Детальный текст", widget=widgets.Textarea)


