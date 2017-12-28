from os.path import join, basename, isfile

import Pyro4
from django.core.files.base import File
from django.db import transaction


from 語料庫.models import 音檔表
from 語料庫.management.commands.匯入1版trs語料 import Command as trs指令
from 程式.提出通用音標 import 提出通用音標
from 程式.全漢全羅.原始通用處理 import 原始通用工具
from 檢查.praat檢查 import praat檢查
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚


class Command(trs指令):
    工具 = Pyro4.Proxy("PYRONAME:校對工具")

    def add_arguments(self, parser):
        parser.add_argument(
            'textgrid資料夾所在', type=str
        )
        parser.add_argument(
            'wav資料夾所在', type=str
        )
        parser.add_argument(
            '資料夾名', type=str
        )
        parser.add_argument(
            '聽拍檔名', type=str
        )
        parser.add_argument(
            'wav檔名', type=str
        )

    @transaction.atomic()
    def handle(self, *args, **參數):
        if basename(參數['textgrid資料夾所在'].rstrip('/')) != 'Praat當佇改佮改好的':
            raise ValueError('textgrid資料夾所在應該是「Praat當佇改佮改好的」')
        if basename(參數['wav資料夾所在'].rstrip('/')) != 'Finished':
            raise ValueError('wav資料夾所在資料夾所在應該是「Finished」')
        textgird檔名 = join(參數['textgrid資料夾所在'], 參數['資料夾名'], 參數['聽拍檔名'])
        wav檔名 = join(參數['wav資料夾所在'], 參數['資料夾名'], 參數['wav檔名'])
        if not isfile(wav檔名):
            raise FileNotFoundError('無wav檔案：{}'.format(wav檔名))
        音檔資料 = 音檔表.objects.create(
            類別=self.語料類別[參數['資料夾名']],
            資料夾名=參數['資料夾名'],
            聲音檔名=basename(wav檔名),
            聽拍檔名=basename(textgird檔名),
        )
        檢查 = praat檢查()
        檢查.檢查檔案(textgird檔名)
        if 檢查.有錯誤無():
            print(檢查.錯誤資訊())
        else:
            語者資料 = 檢查.提出語者資料(textgird檔名)
            for 開始, 結束, 聽拍 in 檢查.提出聽拍資料(textgird檔名):
                原始通用 = 提出通用音標.揣音標(聽拍)
                原始口語調臺羅, 漢字, 本調, 口語調臺羅 = self.原始通用得著臺羅漢字(原始通用)
                語者 = self.揣語者(語者資料, 開始)
                print(原始通用, 漢字, 本調, 口語調臺羅, 語者)
                音檔資料.資料.create(
                    聲音開始時間=開始,
                    聲音結束時間=結束,

                    語者=語者,
                    頭一版資料=聽拍,
                    頭一版通用=原始通用,
                    頭一版轉出來的口語調臺羅=原始口語調臺羅,
                    漢字=漢字,
                    本調臺羅=本調,
                    口語調臺羅=口語調臺羅,

                    sing5hong5舊編號=None,
                    sing5hong5新編號=None,
                    sing5hong5有揀出來用無=False,
                    愛先做無=self.判斷先愛先做無(漢字),
                )
            with open(wav檔名, 'rb') as 檔案:
                音檔資料.原始檔.save(音檔資料.資料夾名 + '/' + 音檔資料.聲音檔名, File(檔案))

    def 原始通用得著臺羅漢字(self, 原始通用):
        原始口語調臺羅 = (
            原始通用工具.處理做口語調臺羅(原始通用).看型('-', ' ')
            .replace(' - ', '-')
        )
        漢字, 本調 = self.工具.口語標漢字本調(原始口語調臺羅)
        本調 = 本調.replace('*', '')
        口語調臺羅 = self.照本調斷詞(本調, 原始口語調臺羅)
        return 原始口語調臺羅, 漢字, 本調, 口語調臺羅

    def 照本調斷詞(self, 本調, 口語調):
        return (
            拆文分析器.對齊句物件(口語調, 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 本調))
            .看型('-', ' ')
        )

    def 揣語者(self, 語者資料, 聽拍開始):
        for _開始, 結束, 語者 in 語者資料:
            if 結束 > 聽拍開始:
                return 語者
