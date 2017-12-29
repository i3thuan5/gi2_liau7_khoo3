
from django.contrib import admin
from 用字規範.models import 語料庫用字
from 語料庫.models import 語料表


class 語料庫用字管理(admin.ModelAdmin):
    list_display = ['id', '漢字', '羅馬字', '出處', '備註', '修改時間']
    exclude = ['分詞']
    ordering = ['-id']
    search_fields = ['id', '漢字', '羅馬字', '分詞', ]

    actions = ['自動檢查重做_愛五分鐘', ]

    def 自動檢查重做_愛五分鐘(self, request, queryset):
        self._重做()

    def _重做(self):
        for 語料 in 語料表.objects.all():
            語料.save()


admin.site.register(語料庫用字, 語料庫用字管理)
