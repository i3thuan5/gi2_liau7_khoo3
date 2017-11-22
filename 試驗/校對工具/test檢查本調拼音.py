from django.test.testcases import TestCase
from 校對工具.檢查本調拼音 import 檢查本調拼音
from 校對工具.檢查本調拼音 import 判斷本調拼音


class 檢查本調拼音試驗(TestCase):

    def test本調拼音正確(self):
        漢字 = '媠的'
        本調臺羅 = 'sui2-e5'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), [])

    def test本調拼音錯誤(self):
        漢字 = '媠的'
        本調臺羅 = 'sui-e5'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), ['媠｜sui1'])

    def test本調輕聲詞正確(self):
        漢字 = '後擺乎'
        本調臺羅 = 'au7-pai2--honnh4'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), [])

    def test本調輕聲詞錯誤(self):
        漢字 = '後擺啦'
        本調臺羅 = 'au7-pai2 lah'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), ['啦｜lah4'])

    def test句首輕聲詞正確(self):
        漢字 = '乎，後擺'
        本調臺羅 = '--Honnh4, au7-pai2'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), [])

    def test句首輕聲詞正確2(self):
        # TODO:
        # 教典例句的書寫規則允許句首輕聲詞不用--，
        # 但往後將此test判定為錯誤
        漢字 = '乎，後擺'
        本調臺羅 = 'Honnh4, au7-pai2'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), [])

    def test漢字少字(self):
        漢字 = '後擺'
        本調臺羅 = 'au7-pai2--honnh4'
        self.assertEqual(
            檢查本調拼音(漢字, 本調臺羅),
            "詞組內底的型「後擺」比音「au7-pai2 0honnh4」少"
        )

    def test漢字少字2(self):
        漢字 = '來dddd'
        本調臺羅 = 'lai5 test  ttt'
        self.assertEqual(
            檢查本調拼音(漢字, 本調臺羅),
            "詞組內底的型「來dddd」比音「lai5 test ttt」少"
        )

    def test判斷本調拼音正確(self):
        漢字 = '媠的'
        本調臺羅 = 'sui2-e5'
        self.assertEqual(判斷本調拼音(漢字, 本調臺羅), '')
    
    def test判斷本調拼音錯誤(self):
        漢字 = '媠的'
        本調臺羅 = 'sui-e5'
        self.assertEqual(判斷本調拼音(漢字, 本調臺羅), '媠｜sui1')
    
    def test判斷本調拼音錯誤2(self):
        漢字 = '駝駝駝'
        本調臺羅 = 'sui2'
        self.assertEqual(判斷本調拼音(漢字, 本調臺羅), '媠｜sui1')