from os.path import join
from tempfile import TemporaryDirectory
from unittest.case import TestCase

from django.core.management import call_command
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 語言模型.models import 語言模型表
from 口語辭典.揣全漢全羅 import 口語揣全漢全羅


class 全漢全羅試驗(TestCase):
    火車 = '我｜gua2 坐-佇｜tse7-ti7 火｜hue2 車｜tshia1 頂｜ting2'
    花車 = '我｜gua2 坐-佇｜tse7-ti7 花｜hue1 車｜tshia1 頂｜ting2'

    def test_火車(self):
        語言模型表.objects.get_or_create(分詞=self.火車)
        語言模型表.objects.get_or_create(分詞=self.花車)
        語言模型表.objects.get_or_create(
            分詞='我｜gua2 佇｜ti7 火｜hue2 車｜tshia1 頭'
        )
        with TemporaryDirectory() as 資料夾:
            with self.settings(GI2_GIAN5_MOO5_HING5=join(資料夾, '語言模型.arpa')):
                call_command('訓練語言模型')
                全漢全羅 = 口語揣全漢全羅()
                原本 = 'hue1-tshia1'
                句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
                self.assertEqual(句物件.看分詞(), '火｜hue2 車｜tshia1')

    def test_花車(self):
        語言模型表.objects.get_or_create(分詞=self.火車)
        語言模型表.objects.get_or_create(分詞=self.花車)
        語言模型表.objects.get_or_create(
            分詞='我｜gua2 有｜u7 花｜hue1 車｜tshia1 的｜e5 相-片｜siong3-pinn3'
        )
        with TemporaryDirectory() as 資料夾:
            with self.settings(GI2_GIAN5_MOO5_HING5=join(資料夾, '語言模型.arpa')):
                call_command('訓練語言模型')

                全漢全羅 = 口語揣全漢全羅()
                原本 = 'hue1-tshia1'
                句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
                self.assertEqual(句物件.看分詞(), '花｜hue1 車｜tshia1')

    def test_喉入聲(self):
        語言模型表.objects.get_or_create(分詞=self.火車)
        語言模型表.objects.get_or_create(
            分詞='你｜li2 閣｜koh4 來｜lai5'
        )
        語言模型表.objects.get_or_create(分詞=self.花車)

        with TemporaryDirectory() as 資料夾:
            with self.settings(GI2_GIAN5_MOO5_HING5=join(資料夾, '語言模型.arpa')):
                call_command('訓練語言模型')

                全漢全羅 = 口語揣全漢全羅()
                原本 = 'li1 koh8 lai5'
                句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
                self.assertEqual(句物件.看分詞(), '你｜li2 閣｜koh4 來｜lai5')

    def test_無佇語料出現的音(self):
        全漢全羅 = 口語揣全漢全羅()
        原本 = 'sui2'
        句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
        self.assertEqual(句物件.看分詞(), 'sui2｜sui2')

    def test_無合法音標(self):
        全漢全羅 = 口語揣全漢全羅()
        原本 = 'Pigu'
        句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
        self.assertEqual(句物件.看分詞(), 'Pigu｜Pigu')
