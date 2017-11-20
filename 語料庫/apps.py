from os.path import join
from tempfile import TemporaryDirectory

from django.apps import AppConfig
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from django.db.models import signals
from 語料庫.signals.新增對齊狀態 import 新增對齊狀態


class 語料庫Config(AppConfig):
    name = '語料庫'

    def ready(self):
        with TemporaryDirectory() as 資料夾:
            檔名 = join(資料夾, 'audio.wav')
            音檔 = 聲音檔.對參數轉(2, 8000, 1, b'sui2')
            with open(檔名, 'wb') as 檔案:
                檔案.write(音檔.wav格式資料())
            try:
                程式腳本._走指令(['normalize-audio', 檔名])
            except RuntimeError:
                raise OSError(
                    '請裝normalize-audio!! '
                    '`sudo apt-get install normalize-audio`'
                )
            try:
                程式腳本._走指令(['sox', 檔名, '-t', 'wav', '/dev/null', 'remix', '1'],)
            except RuntimeError:
                raise OSError('請裝sox!! `sudo apt-get install sox`')
        
        # importing model classes
        from .models import 語料表
        語料表 = self.get_model('語料表')

        # registering signals
        signals.post_save.connect(新增對齊狀態, sender='語料庫.語料表', weak=False,
                                  dispatch_uid='models.新增對齊狀態')