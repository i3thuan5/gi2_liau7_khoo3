# from 語料庫.models import 語料狀況表
from 語料庫.models import 語料表
from 語料庫.管理.校對 import 校對表管理
from django.utils.timezone import now
from 語料庫.widgets.目標音檔欄 import 目標音檔欄
# from 語料庫.管理.檢查 import 檢查表管理


class Kaldi篩掉表(語料表):

    class Meta:
        proxy = True
        verbose_name = "Kaldi篩掉表"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Kaldi篩掉表管理(校對表管理, 目標音檔欄):
    # change list
    list_display = [
        'id',
        '目標音檔',
        '漢字', '本調臺羅', '口語調臺羅',
        '頭一版資料'
    ]
    ordering = ['id']
    list_per_page = 10
    actions = []
    list_filter = ()
    list_display_links = None

    def get_queryset(self, request):
        qs = super(校對表管理, self).get_queryset(request)
        return qs.filter(sing5hong5有揀出來用無=False)
