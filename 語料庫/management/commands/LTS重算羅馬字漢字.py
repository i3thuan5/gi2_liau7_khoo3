import Pyro4
from django.core.management.base import BaseCommand
from django.db import transaction


from 程式.全漢全羅.原始通用處理 import 原始通用工具
from 語料庫.models import 語料表


class Command(BaseCommand):

    @transaction.atomic()
    def handle(self, *args, **參數):
        工具 = Pyro4.Proxy("PYRONAME:校對工具")
        for 語料 in (
            語料表.objects
            .filter(校對者__isnull=False)
            .filter(音檔__聲音檔名='LTS30.wav')
        ):
            原始口語調臺羅 = (
                原始通用工具.處理做口語調臺羅(語料.頭一版通用).看型('-', ' ')
                .replace(' - ', '-')
            )
            漢字, 本調 = 工具.口語標漢字本調(原始口語調臺羅)
            口語調臺羅 = self.照本調斷詞(本調, 原始口語調臺羅)
            print(漢字, 本調, 口語調臺羅)
            語料.漢字 = 漢字
            語料.本調臺羅 = 本調
            語料.口語調臺羅 = 口語調臺羅
            語料.save()
