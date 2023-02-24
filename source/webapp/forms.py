from django import forms
from django.core.exceptions import ValidationError

from django.forms import widgets


from webapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("status", "text", "detail_text")
        labels = {
            'status': 'Статус',
            'text': 'Текст',
            'detail_text': 'Детальный текст',
        }

    def clean_title(self):
        text = self.cleaned_data.get("text")
        if len(text) <= 2:
            raise ValidationError("Заполните линию")
        return text
