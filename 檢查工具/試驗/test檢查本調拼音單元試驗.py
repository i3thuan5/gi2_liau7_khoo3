from django.test.testcases import TestCase
from 檢查工具.檢查本調拼音 import 檢查本調拼音
from 檢查工具.檢查本調拼音 import 判斷本調拼音


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

    def test句首輕聲詞沒有輕聲符號(self):
        # 教典例句的書寫規則允許句首輕聲詞不用--，
        # 但目前將此test判定為錯誤
        漢字 = '乎，後擺'
        本調臺羅 = 'Honnh4, au7-pai2'
        self.assertEqual(檢查本調拼音(漢字, 本調臺羅), ['乎｜honnh4'])

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

    def test判斷合音(self):
        漢字 = '（媠媠）的'
        本調臺羅 = 'sui9-e5'
        self.assertEqual(判斷本調拼音(漢字, 本調臺羅), '')

    def test判斷本調拼音錯誤(self):
        漢字 = '媠的'
        本調臺羅 = 'sui-e5'
        self.assertEqual(判斷本調拼音(漢字, 本調臺羅), '媠｜sui1')

    def test判斷本調拼音錯誤2(self):
        漢字 = '駝駝駝'
        本調臺羅 = 'sui2'
        self.assertIn('濟', 判斷本調拼音(漢字, 本調臺羅))
