from django.test.testcases import TestCase
from 語料庫.models import 音檔表
from 語料庫.管理.校對 import 校對表


class 標本調試驗(TestCase):

    def tearDown(self):
        self.assertEqual(
            標本調(self.漢字, self.原本本調),
            self.答案本調
        )

    def test查詞典處理(self):
        self.漢字 = '媠'
        self.原本本調 = 'sui3'
        self.答案本調 = 'sui2'

    def test照詞處理(self):
        self.漢字 = '大人'
        self.原本本調 = 'tai7-lan5'
        self.答案本調 = 'tai7-lin5'
