import json
from os.path import join, basename

from django.core.files.base import File
from django.db import transaction

from praatio.tgio import openTextgrid


from 語料庫.models import 音檔表
from 語料庫.management.commands.匯入1版trs語料 import Command as trs指令


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

    @transaction.atomic()
    def handle(self, *args, **參數):
        textgird檔名 = join(參數['textgrid資料夾所在'], 參數['資料夾名'], 參數['聽拍檔名'])
        wav檔名 = join(參數['wav資料夾所在'], 參數['資料夾名'],
                     參數['聽拍檔名'].split('|')[0].replace('&amp;', '&'))
        音檔資料 = 音檔表.objects.create(
            類別=self.語料類別[參數['資料夾名']],
            資料夾名=參數['資料夾名'],
            聲音檔名=basename(wav檔名),
            聽拍檔名=basename(textgird檔名),
        )
        tg = openTextgrid(textgird檔名)

        print(tg.tierNameList)
        # Get all intervals
        entryList = tg.tierDict["Speech"].entryList[:10]
        print(entryList)
        a,b,c=entryList[0]
        print(a,b,c)

        entryList = tg.tierDict["Turns"].find("添福")[:10]  # Get all instances of 'a'
        print(entryList)
        print( tg.tierDict["Turns"].entryList[41])
        
        raise NotImplementedError()
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
                愛先做無=self.判斷先愛先做無(一句["漢字"]),
            )
        with open(wav檔名, 'rb') as 檔案:
            音檔資料.原始檔.save(資料夾名 + '/' + 聲音檔名, File(檔案))
