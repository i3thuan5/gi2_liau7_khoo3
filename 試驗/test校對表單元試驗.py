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
#         print('self.語料', self.語料.__dict__)
    
    def test更新校對時間(self):
#         print('33 對齊狀態表數量=', len(對齊狀態表.objects.all()))

        校對資料 = 校對表.objects.get(pk=self.語料.pk)
        print('校對資料.__dict__=', 校對資料.__dict__)
#         一狀態 = 對齊狀態表(狀態='媠｜sui22')
#         一狀態.save()
#         校對資料.對齊狀態 = 一狀態
#         校對資料.save()
#         
#         print('校對資料.__dict__=', 校對資料.__dict__)
#         return

        校對資料.漢字 = '駝'
        self.assertIsNone(
            校對資料.校對時間
        )
        校對資料.save()
        self.assertIsNotNone(
            校對資料.校對時間
        )
#         print('44 對齊狀態表數量=', len(對齊狀態表.objects.all()))

    def test新校對有初始對齊狀態(self):
#         print('47 對齊狀態表數量=', len(對齊狀態表.objects.all()))
        一校對 = 校對表.objects.get(pk=self.語料.pk)
        print('一校對.__dict__=', 一校對.__dict__)
        self.assertIsNotNone(
            一校對.對齊狀態.狀態
        )
    
#     def test更新對齊狀態(self):
#         self.fail()