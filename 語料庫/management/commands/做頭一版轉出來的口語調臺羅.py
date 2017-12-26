from django.db import transaction


from 語料庫.management.commands.匯入1版trs語料 import Command as trs指令
from 程式.全漢全羅.原始通用處理 import 原始通用工具
from 語料庫.models import 語料表


class Command(trs指令):

    @transaction.atomic()
    def handle(self, *args, **參數):
        for 資料 in 語料表.objects.all():
            原始口語調臺羅 = (
                原始通用工具.處理做口語調臺羅(資料.頭一版通用).看型('-', ' ')
                .replace(' - ', '-')
            )
            資料.頭一版轉出來的口語調臺羅 = 原始口語調臺羅
            資料.save()
