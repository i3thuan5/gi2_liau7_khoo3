from 語料庫.models import 語料狀況表


class 檢查表(語料表):
    class Meta:
        proxy = True
        verbose_name = "檢查表"
        verbose_name_plural = verbose_name


class 檢查表管理(語料表管理):
    readonly_fields = ('音檔', '漢字', '本調臺羅', '口語調臺羅', )

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

    actions = [
        '設定無問題',
    ]

    def 設定無問題(self, request, queryset):
        queryset.update(檢查者=request.user)

    def save_model(self, request, obj, form, change):
        # 儲存校對者
        obj.狀況.add(語料狀況表.objects.get(狀況='愛討論'))
        super(檢查表管理, self).save_model(request, obj, form, change)
