
import json
from os.path import join, abspath

from django.conf import settings
from django.core.management.base import BaseCommand


from 語料庫.models import 音檔表
from 語料庫.models import 語料狀況表


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--輸出檔名',
            type=str,
            default='twisas2.json',
        )

    def handle(self, *args, **參數):
        語料狀況表.檢查狀況有著無()
        無愛狀況 = 語料狀況表.無愛的狀況id()
        匯出資料 = []
        for 音檔資料 in 音檔表.objects.order_by('id'):
            語句 = []
            for 資料 in (
                音檔資料.資料
                .filter(校對者__isnull=False)
                .exclude(語料狀況__in=無愛狀況)
            ):
                語句.append({
                    "結束時間": 資料.聲音結束時間,
                    "開始時間": 資料.聲音開始時間,
                    "語者": 資料.語者,
                    "漢字": 資料.漢字,
                    '本調臺羅': 資料.本調臺羅,
                    "口語臺羅": 資料.口語調臺羅,
                    "內容": 資料.口語調臺羅,
                })
            匯出資料.append({
                '影音所在': join(abspath(settings.MEDIA_ROOT), 音檔資料.原始檔.name),
                '聽拍資料': 語句
            })
        with open(參數['輸出檔名'], 'w') as 檔案:
            json.dump(匯出資料, 檔案, ensure_ascii=False, indent=2, sort_keys=True)
