
from django.test.testcases import TestCase
from 語料庫.praat檢查 import praat檢查


class textgrid試驗(TestCase):

    def setUp(self):
        self.檢查 = praat檢查()

    def test_語者時間正常(self):
        self.檢查.檢查語者(
            [
                ('0', '10', 'tsit8'),
                ('10', '20', 'nng7'),
                ('20', '30', 'sann1')
            ],
            [
                ('0', '20', '麗芸'),
                ('20', '30', '添福'),
            ],
        )
        self.assertEqual(len(self.檢查.錯誤), 0)

    def test_語者時間無對著(self):
        self.檢查.檢查語者(
            [
                ('0', '10', 'tsit8'),
                ('10', '20', 'nng7'),
                ('20', '30', 'sann1'),
            ],
            [
                ('0', '20.3', '麗芸'),
                ('20.3', '30', '添福'),
            ],
        )
        self.assertEqual(len(self.檢查.錯誤), 1)
