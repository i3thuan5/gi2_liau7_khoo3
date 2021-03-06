import re

from django.db import models


from 語料庫.models import 語料表
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 檢查工具.檢查本調拼音 import 判斷本調拼音


class 對齊狀態表(models.Model):
    語料 = models.OneToOneField(
        語料表, default=None, related_name='對齊狀態', on_delete=models.CASCADE
    )
    漢字本調對應 = models.CharField(max_length=30)
    本調口語調對應 = models.CharField(max_length=100)
    本調空白 = models.CharField(max_length=30)
    口語調空白 = models.CharField(max_length=30)
    口語調輕聲符 = models.CharField(max_length=30)

    連字符邊仔空白 = re.compile('([\w]+\s+-+)|(-+\s+[\w]+)')
    頭前毋是音標的輕聲 = re.compile('([^a-z0-9]+\s+--)')

    def __str__(self):
        return '\n'.join([
            self.本調空白,
            self.口語調空白,
            self.口語調輕聲符,
            self.漢字本調對應,
            self.本調口語調對應,
        ]).strip()

    def save(self, *args, **kwargs):
        self.漢字本調對應 = 判斷本調拼音(self.語料.漢字, self.語料.本調臺羅)
        self.本調空白 = self.檢查連字符邊仔有空白無(self.語料.本調臺羅)
        self.口語調空白 = self.檢查連字符邊仔有空白無(self.語料.口語調臺羅)
        self.口語調輕聲符 = self.口語調無輕聲連字符(self.語料.口語調臺羅)
        self.本調口語調對應 = self.檢查本調口語調對應(self.語料.本調臺羅, self.語料.口語調臺羅)
        super().save(*args, **kwargs)

    @classmethod
    def 檢查連字符邊仔有空白無(cls, 羅馬字):
        結果 = []
        所在 = 0
        while True:
            揣 = cls.連字符邊仔空白.search(羅馬字, 所在)
            if 揣:
                if not cls.頭前毋是音標的輕聲.search(揣.group(0)):
                    結果.append('「{}」'.format(揣.group(0)))
                所在 = 揣.end(0) - 1
                while 所在 < len(羅馬字) - 1 and 羅馬字[所在] != ' ':
                    所在 -= 1
            else:
                break
        return '、'.join(結果)

    @classmethod
    def 口語調無輕聲連字符(cls, 羅馬字):
        if '--' in 羅馬字:
            return '口語調袂使有輕聲符'
        return ''

    @classmethod
    def 檢查本調口語調對應(cls, 本調臺羅, 口語調臺羅):
        try:
            句物件 = 拆文分析器.對齊句物件(
                文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 本調臺羅),
                文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 口語調臺羅)
            )
        except Exception as 錯誤:
            return str(錯誤).split('！')[0]
        錯誤結果 = []
        for 字物件 in 句物件.篩出字物件():
            if not 字物件.音標敢著(臺灣閩南語羅馬字拼音) and 字物件.型 != 字物件.音:
                錯誤結果.append('「{}」'.format(字物件.看音()))
        return '、'.join(錯誤結果)
