from django.test.testcases import TestCase
from 用字規範.models import 語料庫用字


class 加資料試驗(TestCase):
    def test_加一个教典無的字(self):
        漢字 = '百'
        羅馬字 = 'ah4'
        self.assertTrue(語料庫用字.加字(漢字, 羅馬字))

    def test_加一个教典有的字(self):
        漢字 = '百'
        羅馬字 = 'pah4'
        self.assertFalse(語料庫用字.加字(漢字, 羅馬字))

    def test_重加第二擺(self):
        語料庫用字.加字('百', 'ah4')
        self.assertFalse(語料庫用字.加字('百', 'ah'))
