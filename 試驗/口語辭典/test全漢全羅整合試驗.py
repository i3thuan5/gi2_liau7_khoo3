from os.path import join
from tempfile import TemporaryDirectory

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test.testcases import TestCase


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 語言模型.models import 語言模型表
from 校對工具.views import 工具
from 語料庫.models import 音檔表


class 全漢全羅試驗(TestCase):
    火車 = '我｜gua2 坐-佇｜tse7-ti7 火｜hue2 衫｜sann1 頂｜ting2'
    花車 = '我｜gua2 坐-佇｜tse7-ti7 花｜hue1 衫｜sann1 頂｜ting2'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('教典匯入本調辭典')
        call_command('本調辭典轉口語辭典')

    def test_火車(self):
        語言模型表.objects.get_or_create(分詞=self.火車)
        語言模型表.objects.get_or_create(分詞=self.花車)
        語言模型表.objects.get_or_create(
            分詞='我｜gua2 佇｜ti7 火｜hue2 衫｜sann1 頭'
        )
        with TemporaryDirectory() as 資料夾:
            with self.settings(GI2_GIAN5_MOO5_HING5=join(資料夾, '語言模型.arpa')):
                call_command('訓練語言模型')
                全漢全羅 = 工具()
                原本 = 'hue1-sann1'
                句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
                self.assertEqual(句物件.看分詞(), '火｜hue2 衫｜sann1')

    def test_花車(self):
        語言模型表.objects.get_or_create(分詞=self.火車)
        語言模型表.objects.get_or_create(分詞=self.花車)
        語言模型表.objects.get_or_create(
            分詞='我｜gua2 有｜u7 花｜hue1 衫｜sann1 的｜e5 相-片｜siong3-pinn3'
        )
        with TemporaryDirectory() as 資料夾:
            with self.settings(GI2_GIAN5_MOO5_HING5=join(資料夾, '語言模型.arpa')):
                call_command('訓練語言模型')

                全漢全羅 = 工具()
                原本 = 'hue1-sann1'
                句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
                self.assertEqual(句物件.看分詞(), '花｜hue1 衫｜sann1')

    def test_喉入聲(self):
        語言模型表.objects.get_or_create(分詞=self.火車)
        語言模型表.objects.get_or_create(
            分詞='你｜li2 閣｜koh4 來｜lai5'
        )
        語言模型表.objects.get_or_create(分詞=self.花車)

        with TemporaryDirectory() as 資料夾:
            with self.settings(GI2_GIAN5_MOO5_HING5=join(資料夾, '語言模型.arpa')):
                call_command('訓練語言模型')

                全漢全羅 = 工具()
                原本 = 'li1 koh8 lai5'
                句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
                self.assertEqual(句物件.看分詞(), '你｜li2 閣｜koh4 來｜lai5')

    def test_無佇語料出現的音(self):
        全漢全羅 = 工具()
        原本 = 'sui9'
        句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
        self.assertEqual(句物件.看分詞(), 'sui9｜sui9')

    def test_無合法音標(self):
        全漢全羅 = 工具()
        原本 = 'Pigu'
        句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
        self.assertEqual(句物件.看分詞(), 'Pigu｜Pigu')

    def test_語助詞照校對來調整(self):
        self.加資料()
        call_command('校對語句匯口語辭典')

        全漢全羅 = 工具()
        原本 = 'ooh10'
        句物件 = 全漢全羅.變調臺羅轉本調臺羅(拆文分析器.建立句物件(原本))
        self.assertEqual(句物件.看分詞(), '喔｜ooh4')

    def 加資料(self):
        音檔資料 = 音檔表.objects.create(
            類別='戲劇',
            資料夾名='dirsui2',
            聲音檔名='sui2.wav',
            聽拍檔名='sui2.txt',
        )
        self.語料 = 音檔資料.資料.create(
            聲音結束時間='0',
            聲音開始時間='1',

            語者='sui2',
            頭一版資料='sui2',
            頭一版通用='sui',
            漢字='是喔',
            本調臺羅='si7--ooh4',
            口語調臺羅='si7 ooh10',

            sing5hong5舊編號='333',
            sing5hong5新編號='333',
            sing5hong5有揀出來用無=True,

            校對者=User.objects.create_user('admin', 'admin@test.com', 'pass')
        )
