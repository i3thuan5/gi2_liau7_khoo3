import json
from os.path import basename, dirname

from django.core.files.base import File
from django.core.management.base import BaseCommand
from django.db import transaction


from 程式.全漢全羅.匯入檔案揣資料夾 import 揣資料夾內的語料
from 語料庫.models import 音檔表


class Command(BaseCommand):
    語料類別 = {
        'MH': '戲劇',
        'DaAi_blktc': '戲劇',
        'DaAi_csgr': '戲劇',
        'DaAi_urs': '戲劇',
        'DaAi_vvrs': '戲劇',
        'LTS': '戲劇',
    }

    def add_arguments(self, parser):
        parser.add_argument(
            'json資料夾所在', type=str
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

    @transaction.atomic()
    def handle(self, *args, **參數):
        for json檔名, wav檔名 in 揣資料夾內的語料(參數['json資料夾所在'], 參數['wav資料夾所在']):
            if (
                basename(dirname(json檔名)) == 參數['資料夾名'] and
                basename(json檔名) == 參數['聽拍檔名']
            ):
                類別 = self.語料類別[參數['資料夾名']]
                資料夾名 = basename(dirname(wav檔名))
                聲音檔名 = basename(wav檔名)
                聽拍檔名 = basename(json檔名)
                音檔資料 = 音檔表.objects.create(
                    類別=類別,
                    資料夾名=資料夾名,
                    聲音檔名=聲音檔名,
                    聽拍檔名=聽拍檔名,
                )
                with open(wav檔名, 'rb') as 檔案:
                    音檔資料.原始檔.save(資料夾名 + '/' + 聲音檔名, File(檔案))
                with open(json檔名) as json檔案:
                    for 一句 in json.load(json檔案):
                        音檔資料.資料.create(
                            聲音結束時間=一句["結束時間"],
                            聲音開始時間=一句["開始時間"],

                            語者=一句["語者"],
                            頭一版資料=一句["trs聽拍"],
                            頭一版通用=一句["原始通用"],
                            漢字=一句["漢字"],
                            本調臺羅=一句["臺羅"],
                            口語調臺羅=一句["口語調臺羅"],

                            sing5hong5舊編號=一句["舊編號"],
                            sing5hong5新編號=一句["新編號"],
                            sing5hong5有揀出來用無=一句["有揀出來無"],
                        )
