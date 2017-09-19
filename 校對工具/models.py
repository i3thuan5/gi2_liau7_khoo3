from django.db import models


class 辭典表(models.Model):
    分詞 = models.CharField(
        max_length=100,
        unique=True,
    )

    @classmethod
    def 全部分詞(cls):
        return set(cls.objects.all().values_list('分詞', flat=True))


# class 語言模型表(models.Model):
#     分詞 = models.TextField()
