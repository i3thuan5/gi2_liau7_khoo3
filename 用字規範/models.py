import re

from django.db import models


from 用字.models import 用字表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚


class 語料庫用字(models.Model):
    漢字 = models.CharField(max_length=20, db_index=True)
    羅馬字 = models.CharField(max_length=20, db_index=True)
    分詞 = models.CharField(max_length=20, db_index=True)
    出處 = models.TextField()
    備註 = models.TextField(blank=True)

    class Meta:
        verbose_name = "語料庫補字"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.分詞 = 拆文分析器.對齊字物件(
            self.漢字,
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, self.羅馬字)
        ).轉音(臺灣閩南語羅馬字拼音).看分詞()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.分詞

    @classmethod
    def 有這个字無(cls, 字物件):
        if 用字表.有這个字無(字物件):
            return True
        if cls.objects.filter(分詞=字物件.轉音(臺灣閩南語羅馬字拼音).看分詞()).exists():
            return True
        return False

    合音代號 = 'X'
    _代換 = re.compile('（[^）]+）')

    @classmethod
    def 漢字合音轉做代號(cls, 漢字):
        return cls._代換.sub(' ' + cls.合音代號 + ' ', 漢字)

    @classmethod
    def 這字的漢字敢是合音(cls, 字物件):
        return 字物件.型 == cls.合音代號
