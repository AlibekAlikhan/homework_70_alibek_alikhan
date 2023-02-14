from django.db import models


# Create your models here.
class Article(models.Model):
    status = models.CharField(max_length=10, null=False, verbose_name="Статус")
    text = models.TextField(max_length=3000, null=False, verbose_name="Текст")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    end_at = models.DateTimeField(auto_now=True, verbose_name="Дата дедлайна")

    def __str__(self):
        return f"{self.status} - {self.text}"
