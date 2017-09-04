
from django.contrib import admin
from 語料庫.models import 語料表
from 語料庫.models import 語料狀況表
from 語料庫.管理.校對 import 語料表管理
from 語料庫.管理.檢查 import 檢查表
from 語料庫.管理.檢查 import 檢查表管理


admin.site.disable_action('delete_selected')



admin.site.register(語料表, 語料表管理)
admin.site.register(語料狀況表)

admin.site.register(檢查表, 檢查表管理)
