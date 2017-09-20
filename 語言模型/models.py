from django.db import models


class 語言模型表(models.Model):
    分詞 = models.TextField()

    @classmethod
    def 全部分詞(cls):
        return set(cls.objects.all().values_list('分詞', flat=True))
