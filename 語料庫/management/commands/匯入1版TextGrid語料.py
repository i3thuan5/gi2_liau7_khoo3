from os.path import join, basename, isfile

import Pyro4
from django.core.files.base import File
from django.db import transaction


from 語料庫.models import 音檔表
from 語料庫.management.commands.匯入1版trs語料 import Command as trs指令
from 語料庫.praat檢查 import praat檢查
from 程式.提出通用音標 import 提出通用音標
from 程式.全漢全羅.原始通用處理 import 原始通用工具
from 校對工具.views import 工具


class Command(trs指令):

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
            工具 = Pyro4.Proxy("PYRONAME:校對工具")
            語者資料 = 檢查.提出語者資料(textgird檔名)
            for 開始, 結束, 聽拍 in 檢查.提出聽拍資料(textgird檔名):
                原始通用 = 提出通用音標.揣音標(聽拍)
                口語調臺羅 = 原始通用工具.處理做口語調臺羅(原始通用).看型('-', ' ')
                漢字, 本調 = 工具.口語標漢字本調(口語調臺羅)
                print(原始通用, 漢字, 本調, 口語調臺羅)
                音檔資料.資料.create(
                    聲音結束時間=開始,
                    聲音開始時間=結束,

                    語者=self.揣語者(語者資料, 開始),
                    頭一版資料=聽拍,
                    頭一版通用=原始通用,
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
        raise NotImplementedError()

    def 揣語者(self, 語者資料, 聽拍開始):
        for _開始, 結束, 語者 in 語者資料:
            if 結束 > 聽拍開始:
                return 語者
