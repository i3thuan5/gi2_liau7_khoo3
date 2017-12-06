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

    def test_愛有speech(self):
        self.檢查.檢查有聽拍無()
        self.assertIn('Speech', self.檢查.錯誤資訊())

    def test_愛有turns(self):
        self.檢查.檢查有語者無()
        self.assertIn('Turns', self.檢查.錯誤資訊())
