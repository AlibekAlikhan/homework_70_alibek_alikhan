from django.db import models


class Status(models.Model):
    name = models.CharField(verbose_name="Статус", max_length=30)

    def __str__(self):
        return self.name
