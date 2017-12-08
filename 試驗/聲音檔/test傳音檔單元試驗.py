from django.test.testcases import TestCase
from 語料庫.models import 音檔表
from 語料庫.介面 import 傳音檔
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from django.core.files.base import ContentFile


class 傳音檔試驗(TestCase):

    def test孤聲道(self):
        音檔資料 = 音檔表.objects.create(
            類別='戲劇',
            資料夾名='dirsui2',
            聲音檔名='sui2.wav',
            聽拍檔名='sui2.txt',
        )
        音檔 = 聲音檔.對參數轉(2, 16000, 2, b'sui2' * 33333)
        音檔資料.原始檔.save('sui2.wav', ContentFile(音檔.wav格式資料()))

        回應 = 傳音檔(None, 音檔資料.id, 0.3, 0.33)
        回應音檔 = 聲音檔.對資料轉(回應.content)
        self.assertEqual(回應音檔.幾个聲道, 1)
