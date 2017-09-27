from 語料庫.管理.校對 import 校對表管理
from 語料庫.管理.校對 import 校對表
from 語料庫.widgets.目標音檔欄 import 目標音檔欄


class 討論表(校對表):

    class Meta:
        proxy = True
        verbose_name = "討論表"
        verbose_name_plural = verbose_name


class 討論表管理(校對表管理, 目標音檔欄):
    # change list
    list_display = [
        'id',
        '目標音檔', 
        '狀況',
        '漢字', '本調臺羅', '口語調臺羅',
        '備註開頭',
        '校對者', '校對時間'
    ]

    def get_queryset(self, request):
        qs = super(校對表管理, self).get_queryset(request)
        return qs.filter(語料狀況__狀況="愛討論")
