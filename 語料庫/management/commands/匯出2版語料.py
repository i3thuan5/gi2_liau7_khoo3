
import json
from os.path import join, abspath

from django.conf import settings
from django.core.management.base import BaseCommand


from 語料庫.models import 音檔表


class Command(BaseCommand):
    預設檔名 = 'twisas2.json'

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
            for 資料 in (
                音檔資料.資料
                .filter(校對者__isnull=False)
                .exclude(語料狀況__確定有校對=False)
                .exclude(語料狀況__Kaldi輸出=False)
            ):
                語句.append(self.轉做json(資料))
                語句數量 += 1
                語句秒數 += 資料.聲音結束時間 - 資料.聲音開始時間
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
            "內容": 資料.口語調臺羅,
        }
