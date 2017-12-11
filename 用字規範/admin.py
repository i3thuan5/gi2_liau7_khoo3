
from django.contrib import admin
from 用字規範.models import 語料庫用字


class 語料庫用字管理(admin.ModelAdmin):
    list_display = ['id', '漢字', '羅馬字', '出處', '備註', ]
    ordering = ['-id']
    exclude=['分詞']


admin.site.register(語料庫用字, 語料庫用字管理)
