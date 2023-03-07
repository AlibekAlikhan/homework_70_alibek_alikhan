from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, BaseValidator

from webapp.models import Task


class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value):
        message = "Максимум можно ввести %(limit_value)s символов, а вы ввели %(show_value)s"
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return value > limit_value

    def clean(self, value):
        return len(value)


class ArticleForm(forms.ModelForm):
    text = forms.CharField(
        validators=(MinLengthValidator(limit_value=2, message='Введите больше 2 символов'), CustomLenValidator(30)))
    detail_text = forms.CharField(
        validators=(MinLengthValidator(limit_value=1, message='Введите больше 1 символов'), CustomLenValidator(100)))

    class Meta:
        model = Task
        fields = ("status", "teg", "text", "detail_text")
        labels = {
            'status': 'Статус',
            'text': 'Текст',
            'teg': 'Тег',
            'detail_text': 'Детальный текст',
        }
