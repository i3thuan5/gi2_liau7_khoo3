
import json
from os.path import join, abspath

from django.conf import settings
from django.core.management.base import BaseCommand


from 語料庫.models import 音檔表
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class Command(BaseCommand):
    預設檔名 = 'twisas2trs.json'

    def add_arguments(self, parser):
        parser.add_argument(
            '--輸出檔名',
            type=str,
            default=self.預設檔名,
        )

    def handle(self, *args, **參數):
        語句數量 = 0
        語句秒數 = 0.0
        匯出資料 = []
        for 音檔資料 in 音檔表.objects.order_by('id'):
            語句 = []
            for 資料 in 音檔資料.資料.all():
                try:
                    語句.append(self.轉做json(資料))
                    語句數量 += 1
                    語句秒數 += 資料.聲音結束時間 - 資料.聲音開始時間
                except Exception as 錯誤:
                    print(錯誤)
            if len(語句) > 0:
                匯出資料.append({
                    '影音所在': join(abspath(settings.MEDIA_ROOT), 音檔資料.原始檔.name),
                    '聽拍資料': 語句
                })
        with open(參數['輸出檔名'], 'w') as 檔案:
            json.dump(匯出資料, 檔案, ensure_ascii=False, indent=2, sort_keys=True)
        self.stdout.write('攏總{}檔案、{}句、{}秒'.format(len(匯出資料), 語句數量, 語句秒數))

    def 轉做json(self, 資料):
        return {
            "結束時間": 資料.聲音結束時間,
            "開始時間": 資料.聲音開始時間,
            "語者": 資料.語者,
            "漢字": 資料.漢字,
            '本調臺羅': 資料.本調臺羅,
            "口語臺羅": 資料.口語調臺羅,
            "內容": 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 資料.口語調臺羅),
            '備註': 資料.備註,
            '校對者': str(資料.校對者),
            '語料狀況': sorted(資料.語料狀況.all().values_list('pk', flat=1)),
        }
