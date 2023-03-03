from django.db import models
from django.utils import timezone


class Article(models.Model):
    status = models.ForeignKey('webapp.Status', related_name='articles', on_delete=models.CASCADE, verbose_name="Статус")
    teg = models.ManyToManyField(to="webapp.Teg", related_name="articles", blank=True)
    text = models.TextField(max_length=3000, null=True, verbose_name="Текст")
    detail_text = models.TextField(max_length=3000, null=True, verbose_name="Детальный текст")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    update_at = models.DateTimeField(verbose_name="Дата удаления", null=True, default=None)

    def update(self, using=None, keep_parents=False):
        self.update_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.status} - {self.text}"
