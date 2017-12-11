import re

from django.db import models


class 語料庫用字(models.Model):
    漢字 = models.CharField(max_length=20, db_index=True)
    羅馬字 = models.CharField(max_length=20, db_index=True)
    分詞 = models.CharField(max_length=20, db_index=True)
    出處 = models.TextField()
    備註 = models.TextField()

    合音代號 = 'X'
    _代換 = re.compile('（[^）]+）')

    @classmethod
    def 漢字合音轉做代號(cls, 漢字):
        return cls._代換.sub(' ' + cls.合音代號 + ' ', 漢字)

    @classmethod
    def 這字的漢字敢是合音(cls, 字物件):
        return 字物件.型 == cls.合音代號
