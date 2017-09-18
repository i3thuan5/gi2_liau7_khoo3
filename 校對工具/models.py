from django.db import models


class 辭典表(models.Model):
    分詞 = models.CharField(
        max_length=100,
        unique=True,
    )


class 語言模型表(models.Model):
    分詞 = models.CharField(
        max_length=100,
        unique=True,
    )
