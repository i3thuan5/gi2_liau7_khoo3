

from 語料庫.praat檢查 import praat檢查
from django.test.testcases import TestCase


class textgrid試驗(TestCase):
    def setUp(self):
        self.檢查 = praat檢查()

    def test_袂使有兩組字幕趨線(self):
        self.檢查.檢查聽拍([(('0', '10', '而且我做的料理//大家都吃光光還讚不絕口呢//a1'))])
        self.assertEqual(len(self.檢查.錯誤), 1)

    def test_字幕趨線傷濟(self):
        self.檢查.檢查聽拍([('0', '10', '而且我做的料理//a1 大家都吃光光還讚不絕口呢//a2')])
        self.assertEqual(len(self.檢查.錯誤), 1)

    def test_袂使有noise(self):
        self.檢查.檢查聽拍([('0', '10', '[noise]')])
        self.assertEqual(len(self.檢查.錯誤), 1)

    def test_袂使有empty(self):
        self.檢查.檢查聽拍([('0', '10', '[empty]')])
        self.assertEqual(len(self.檢查.錯誤), 1)

    def test_袂使有silence(self):
        self.檢查.檢查聽拍([('0', '10', '[silence]')])
        self.assertEqual(len(self.檢查.錯誤), 1)

    def test_有ATHL真實愛提出來討論(self):
        self.檢查.檢查聽拍([('0', '10', 'ATHL')])
        self.assertEqual(len(self.檢查.錯誤), 1)
