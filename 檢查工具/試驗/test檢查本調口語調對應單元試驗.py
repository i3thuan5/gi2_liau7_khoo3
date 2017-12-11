from django.test.testcases import TestCase
from 檢查工具.models import 對齊狀態表


class 檢查本調口語調對應單元試驗(TestCase):

    def test拼音正確(self):
        本調臺羅 = 'sui2-e5'
        口語調臺羅 = 'sui2-e5'
        self.assertEqual(對齊狀態表.檢查本調口語調對應(本調臺羅, 口語調臺羅), '')

    def test口語調拼音錯誤(self):
        本調臺羅 = 'sui2-e5'
        口語調臺羅 = 'suii2-e5'
        self.assertEqual(對齊狀態表.檢查本調口語調對應(本調臺羅, 口語調臺羅), '「suii2」')

    def test本調輕聲(self):
        本調臺羅 = 'sui2--e5'
        口語調臺羅 = 'sui2 e3'
        self.assertEqual(對齊狀態表.檢查本調口語調對應(本調臺羅, 口語調臺羅), '')

    def test對無齊(self):
        本調臺羅 = 'sui2 e5,'
        口語調臺羅 = 'sui2 e5'
        self.assertEqual(
            對齊狀態表.檢查本調口語調對應(本調臺羅, 口語調臺羅),
            '詞組內底的型「sui2 e5 , 」比音「sui2 e5」濟'
        )

    def test外來詞無要緊(self):
        本調臺羅 = 'sui2 e5 Pigu 就是你'
        口語調臺羅 = 'sui2 e5 Pigu 就是你'
        self.assertEqual(對齊狀態表.檢查本調口語調對應(本調臺羅, 口語調臺羅), '')
