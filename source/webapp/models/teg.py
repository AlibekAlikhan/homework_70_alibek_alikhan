from django.db import models


class Teg(models.Model):
    name = models.CharField(verbose_name="Тег", max_length=30)

    def __str__(self):
        return self.name
