from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    status = models.CharField(max_length=10, null=False, verbose_name="Статус")
    text = models.TextField(max_length=3000, null=True, verbose_name="Текст")
    detail_text = models.TextField(max_length=3000, null=True, verbose_name="Детальный текст")
    is_deleted = models.BooleanField(verbose_name="удалено", null=False, default=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Дата добавления")
    deleted_at = models.DateField(verbose_name="Дата удаления", null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.status} - {self.text}"
