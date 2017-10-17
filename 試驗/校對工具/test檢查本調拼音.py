from django.test.testcases import TestCase
from 校對工具.檢查本調拼音 import 檢查本調拼音


class 檢查本調拼音試驗(TestCase):

    def test本調拼音正確(self):
        漢字 = '媠的'
        本調臺羅 = 'sui-e5'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), [])

    def test更新對齊狀態_錯誤(self):
        漢字 = '媠的'
        本調臺羅 = 'sui-e5'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), ['媠的'])