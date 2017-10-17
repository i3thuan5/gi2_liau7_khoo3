from django.test.testcases import TestCase
from 校對工具.檢查本調拼音 import 檢查本調拼音


class 檢查本調拼音試驗(TestCase):

    def test本調拼音正確(self):
        漢字 = '媠的'
        本調臺羅 = 'sui2-e5'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), [])

    def test更新對齊狀態錯誤(self):
        漢字 = '媠的'
        本調臺羅 = 'sui-e5'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), ['媠｜sui1'])
    
    def test本調輕聲詞(self):
        漢字 = '後擺乎'
        本調臺羅 = 'au7-pai2--honnh4'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), [])

    def test本調輕聲詞錯誤(self):
        漢字 = '後擺乎'
        本調臺羅 = 'au7-pai2 honnh4'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), ['乎｜honnh4'])
    
    def test本調少字(self):
        漢字 = '後擺'
        本調臺羅 = 'au7-pai2 honnh4'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), ['乎｜honnh4'])