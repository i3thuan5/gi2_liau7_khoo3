from django.db import models
from 語料庫.models import 語料表
import re


class 對齊狀態表(models.Model):
    語料 = models.OneToOneField(
        語料表, default=None, related_name='對齊狀態', on_delete=models.CASCADE
    )
    狀態 = models.CharField(max_length=30)
    本調空白 = models.CharField(max_length=30)
    口語調空白 = models.CharField(max_length=30)
    
    連字符邊仔空白 = re.compile('([\w]+ -+)|(-+ [\w]+)')

    def __str__(self):
        return self.狀態

    def save(self, *args, **kwargs):
        self.本調空白=self.檢查連字符邊仔有空白無(self.語料.本調臺羅)
        self.口語調空白=self.檢查連字符邊仔有空白無(self.語料.口語調臺羅)
        super().save(*args, **kwargs)

    @classmethod
    def 檢查連字符邊仔有空白無(cls, 羅馬字):
        結果 = []
        所在 = 0
        while True:
            揣 = cls.連字符邊仔空白.search(羅馬字, 所在)
            if 揣:
                結果.append('「{}」'.format(揣.group(0)))
                所在 = 揣.end(0) - 1
                while 所在 < len(羅馬字) - 1 and 羅馬字[所在] != ' ':
                    所在 -= 1
            else:
                break
        return '、'.join(結果)
