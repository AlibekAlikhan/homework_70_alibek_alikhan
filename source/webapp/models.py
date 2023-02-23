from django.db import models


# Create your models here.
class Article(models.Model):
    status = models.CharField(max_length=10, null=False, verbose_name="Статус")
    text = models.TextField(max_length=3000, null=True, verbose_name="Текст")
    detail_text = models.TextField(max_length=3000, null=True, verbose_name="Детальный текст")
    create_at = models.DateField(auto_now_add=True, verbose_name="Дата добавления")


    def __str__(self):
        return f"{self.status} - {self.text}"
