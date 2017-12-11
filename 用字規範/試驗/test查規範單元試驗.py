from django.test.testcases import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 用字規範.models import 語料庫用字


class 查規範試驗(TestCase):
    def test_查教典有的字(self):
        漢字 = '百'
        羅馬字 = 'pah4'
        self.assertTrue(語料庫用字.有這个字無(拆文分析器.對齊字物件(漢字, 羅馬字)))

    def test_查新加的字(self):
        漢字 = '百'
        羅馬字 = 'ah4'
        語料庫用字.objects.create(漢字=漢字, 羅馬字=羅馬字)
        self.assertTrue(語料庫用字.有這个字無(拆文分析器.對齊字物件(漢字, 羅馬字)))

    def test_查新輕聲的字(self):
        漢字 = '百'
        羅馬字 = '--ah4'
        語料庫用字.objects.create(漢字=漢字, 羅馬字=羅馬字)
        self.assertTrue(語料庫用字.有這个字無(拆文分析器.對齊字物件(漢字, '0ah4')))
