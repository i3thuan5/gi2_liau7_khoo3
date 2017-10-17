from django.test.testcases import TestCase
from 語料庫.models import 音檔表
from 語料庫.管理.校對 import 校對表


class 校對表試驗(TestCase):

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
        )

    def test更新校對時間(self):
        校對資料 = 校對表.objects.get(pk=self.語料.pk)
        校對資料.漢字 = '駝'
        self.assertIsNone(
            校對資料.校對時間
        )
        校對資料.save()
        self.assertIsNotNone(
            校對資料.校對時間
        )
