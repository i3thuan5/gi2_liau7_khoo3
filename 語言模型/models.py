from os.path import join
from shutil import copyfile
from tempfile import TemporaryDirectory

from django.conf import settings
from django.db import models


from 臺灣言語工具.語言模型.KenLM語言模型訓練 import KenLM語言模型訓練
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型


class 語言模型表(models.Model):
    分詞 = models.TextField()

    @classmethod
    def 全部分詞(cls):
        return set(cls.objects.all().values_list('分詞', flat=True))

    @classmethod
    def 語言模型檔案(cls):
        return settings.GI2_GIAN5_MOO5_HING5

    @classmethod
    def 訓練模型(cls):
        with TemporaryDirectory() as 資料夾:
            語句 = join(資料夾, '語句.txt')
            with open(語句, 'w') as 檔案:
                for 分詞 in cls.全部分詞():
                    print(分詞, file=檔案)
            copyfile(
                KenLM語言模型訓練().訓練(
                    [語句],
                    join(資料夾, '暫存資料夾'),
                    連紲詞長度=3
                ),
                cls.語言模型檔案()
            )

    @classmethod
    def 載入模型(cls):
        return KenLM語言模型(
            cls.語言模型檔案()
        )
