from os.path import join
from tempfile import TemporaryDirectory

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test.testcases import TestCase


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 語言模型.models import 語言模型表
from 校對工具.views import 工具
from 語料庫.models import 音檔表
from 語料庫.praat檢查 import praat檢查


class textgrid試驗(TestCase):
    def setUp(self):
        self.檢查 = praat檢查()

    def test_無錯誤(self):
        self.assertEqual(len(self.檢查.錯誤), 0)

    def test_加一筆錯誤(self):
        self.檢查.發生錯誤('tsit')
        self.assertEqual(len(self.檢查.錯誤), 1)

    def test_加兩筆錯誤(self):
        self.檢查.發生錯誤('tsit')
        self.檢查.發生錯誤('nng')
        self.assertEqual(len(self.檢查.錯誤), 2)

    def test_錯誤資訊(self):
        self.檢查.發生錯誤('tsit')
        self.檢查.發生錯誤('nng')
        self.assertEqual(len(self.檢查.錯誤資訊().split('\n')), 2)
