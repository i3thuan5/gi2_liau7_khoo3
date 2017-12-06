from django.test.testcases import TestCase


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
