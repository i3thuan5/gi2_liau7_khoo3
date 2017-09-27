from django.db import models
from 臺灣言語工具.辭典.型音辭典 import 型音辭典
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.詞 import 詞


class 口語辭典表(models.Model):
    _隔開符號 = ' '
    字分詞陣列 = models.CharField(
        max_length=1000,
        unique=True,
    )

    @classmethod
    def 辭典物件(cls):
        口語辭典 = 型音辭典(4)
        for 分詞 in cls._全部分詞陣列():
            字陣列 = []
            for 字分詞 in 分詞.split(cls._隔開符號):
                字陣列.append(拆文分析器.分詞字物件(字分詞))
            口語辭典.加詞(詞(字陣列))
        return 口語辭典

    @classmethod
    def 匯詞物件(cls, 詞物件):
        字分詞 = []
        for 字物件 in 詞物件.篩出字物件():
            字分詞.append(字物件.看分詞())
        cls.objects.get_or_create(字分詞陣列=cls._隔開符號.join(字分詞))

    @classmethod
    def _全部分詞陣列(cls):
        return cls.objects.all().values_list('字分詞陣列', flat=True)
