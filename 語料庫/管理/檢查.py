
class 檢查表(語料表):
    class Meta:
        proxy = True

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
