from django.test.testcases import TestCase
from 檢查工具.models import 對齊狀態表


class 檢查本調拼音試驗(TestCase):

    def test正常羅馬字(self):
        臺羅 = 'sui2-e5--lah4'
        self.assertEqual(對齊狀態表.檢查連字符邊仔有空白無(臺羅), '')

    def test頭前有空白(self):
        臺羅 = 'sui2 -e5'
        self.assertEqual(對齊狀態表.檢查連字符邊仔有空白無(臺羅), '「sui2 -」')

    def test後壁有空白(self):
        臺羅 = 'sui2- e5'
        self.assertEqual(對齊狀態表.檢查連字符邊仔有空白無(臺羅), '「- e5」')

    def test輕聲符號後壁有空白(self):
        臺羅 = 'sui2-- e5'
        self.assertEqual(對齊狀態表.檢查連字符邊仔有空白無(臺羅), '「-- e5」')

    def test濟个問題(self):
        臺羅 = 'sui2 - e5 -- lah4'
        self.assertEqual(
            對齊狀態表.檢查連字符邊仔有空白無(臺羅),
            '「sui2 -」、「- e5」、「e5 --」、「-- lah4」'
        )
