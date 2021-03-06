from django.test.testcases import TestCase
from 語料庫.models import 音檔表
from 語料庫.管理.檢查 import 檢查表


class 檢查表試驗(TestCase):

    def setUp(self):
        音檔資料 = 音檔表.objects.create(
            類別='戲劇',
            資料夾名='dirsui2',
            聲音檔名='sui2.wav',
            聽拍檔名='sui2.txt',
        )
        self.語料 = 音檔資料.資料.create(
            聲音結束時間='0',
            聲音開始時間='1',

            語者='sui2',
            頭一版資料='sui2',
            頭一版通用='sui',
            漢字='媠',
            本調臺羅='sui2',
            口語調臺羅='sui2',

            sing5hong5舊編號='333',
            sing5hong5新編號='333',
            sing5hong5有揀出來用無=True,
            愛先做無=True,
        )

    def test更新檢查時間(self):
        檢查資料 = 檢查表.objects.get(pk=self.語料.pk)
        檢查資料.漢字 = '駝'
        self.assertIsNone(
            檢查資料.檢查時間
        )
        檢查資料.save()
        self.assertIsNotNone(
            檢查資料.檢查時間
        )
