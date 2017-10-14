
import json
from os.path import join, abspath

from django.conf import settings
from django.core.management.base import BaseCommand


from 語料庫.models import 音檔表
from 語料庫.models import 語料狀況表


class Command(BaseCommand):
    無愛的狀況 = [
        '愛討論',
        '品質：講袂清楚',
        '品質：有人聲雜音',
        '品質：有非人聲雜音',
        '詞：有外語詞',
        '北部腔o',
        '切音問題',
        '猶袂處理好',
        '雜音傷大',
        '重複語料',
    ]

    def add_arguments(self, parser):
        parser.add_argument(
            '--輸出檔名',
            type=str,
            default='twisas2.json',
        )

    def handle(self, *args, **參數):
        無愛狀況 = (
            語料狀況表.objects
            .filter(狀況__in=self.無愛的狀況)
            .values_list('id', flat=True)
        )
        if 無愛狀況.count() != len(self.無愛的狀況):
            拍毋著 = []
            for 狀況 in self.無愛的狀況:
                if not 語料狀況表.objects.filter(狀況=狀況).exists():
                    拍毋著.append(狀況)
            raise RuntimeError('狀況名有拍毋著！！\n{}'.format('\n'.join(拍毋著)))
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
