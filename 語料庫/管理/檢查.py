from 語料庫.models import 語料狀況表
from 語料庫.models import 語料表
from 語料庫.管理.校對 import 校對表管理
from django.utils.timezone import now


class 檢查表(語料表):

    class Meta:
        proxy = True
        verbose_name = "2.檢查表"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.檢查時間 = now()
        super().save(*args, **kwargs)


class 檢查表管理(校對表管理):
    # change list
    list_display = [
        'id',
        '目標音檔', '漢字', '本調臺羅', '口語調臺羅',
        '檢查者', '檢查時間', '校對者', '校對時間',
    ]
    ordering = ['檢查者', 'id']
    list_per_page = 10
    actions = [
        '設定無問題',
    ]

    def 目標音檔(self, obj):
        return ('''<audio controls>
        <source src='/音檔/{}/{}/{}/audio.wav'>
        Your browser does not support the audio element.</audio>'''.format(
            obj.音檔.id, obj.聲音開始時間, obj.聲音結束時間
        ))
    目標音檔.allow_tags = True

    def 設定無問題(self, request, queryset):
        queryset.update(檢查者=request.user, 檢查時間=now())

    # change view
    readonly_fields = ('音檔', '漢字', '本調臺羅', '口語調臺羅', '語料狀況',)
    fieldsets = (
        ('音檔', {
            'fields': ('音檔', ),
            'classes': ['wide']
        }),
        (None, {
            'fields': ('漢字', '本調臺羅', '口語調臺羅', '備註', ),
            'classes': ['wide']
        }),
        (None, {
            'fields': ('語料狀況', ),
            'classes': ['wide']
        }),
    )

    def save_model(self, request, obj, form, change):
        # 儲存校對者
        obj.語料狀況.add(語料狀況表.objects.get(狀況='愛討論'))
        obj.檢查者 = request.user
        super(檢查表管理, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(校對表管理, self).get_queryset(request)
        return qs.filter(校對者__isnull=False)
