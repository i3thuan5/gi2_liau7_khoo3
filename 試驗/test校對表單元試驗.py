from django.test.testcases import TestCase
from 語料庫.models import 音檔表
from 語料庫.管理.校對 import 校對表
from 語料庫.models import 對齊狀態表


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
            愛先做無=True,
        )

    def test更新校對時間(self):
        校對資料 = 校對表.objects.get(pk=self.語料.pk)
        self.assertIsNone(
            校對資料.校對時間
        )
        校對資料.save()
        self.assertIsNotNone(
            校對資料.校對時間
        )

    def test新校對有初始對齊狀態(self):
        一校對 = 校對表.objects.get(pk=self.語料.pk)
        self.assertIsNotNone(
            一校對.對齊狀態
        )
        self.assertEqual(
            一校對.對齊狀態.pk, 1
        )

    def test對齊狀態顯示錯誤(self):
        一校對 = 校對表.objects.get(pk=self.語料.pk)
#         print('1st save=',一校對.__dict__)
        一校對.漢字 = '駝駝駝'
#         print('2nd save')
        一校對.save()
#         print('2nd save=',一校對.__dict__)
        self.assertEqual(
            一校對.對齊狀態.狀態, '型比音多'
        )
        self.assertEqual(
            一校對.對齊狀態.pk, 1
        )
