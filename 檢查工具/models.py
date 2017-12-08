from django.db import models
from 語料庫.models import 語料表


class 對齊狀態表(models.Model):
    語料 = models.OneToOneField(
        語料表, default=None, related_name='對齊狀態', on_delete=models.CASCADE
    )
    狀態 = models.CharField(max_length=30)

    def __str__(self):
        return self.狀態
