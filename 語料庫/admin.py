
from django.contrib import admin
from 語料庫.models import 語料狀況表
from 語料庫.管理.檢查 import 檢查表
from 語料庫.管理.檢查 import 檢查表管理
from 語料庫.管理.校對 import 校對表
from 語料庫.管理.校對 import 校對表管理
from 語料庫.管理.討論 import 討論表
from 語料庫.管理.討論 import 討論表管理
from 語料庫.管理.Kaldi篩掉 import Kaldi篩掉表
from 語料庫.管理.Kaldi篩掉 import Kaldi篩掉表管理


admin.site.disable_action('delete_selected')


admin.site.register(語料狀況表)
admin.site.register(校對表, 校對表管理)
admin.site.register(檢查表, 檢查表管理)
admin.site.register(Kaldi篩掉表, Kaldi篩掉表管理)
admin.site.register(討論表, 討論表管理)
