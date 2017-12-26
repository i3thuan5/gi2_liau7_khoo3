from django.db import transaction


from 語料庫.management.commands.匯入1版TextGrid語料 import Command as textgrid指令
from 語料庫.models import 語料表


class Command(textgrid指令):

    def add_arguments(self, parser):
        pass

    @transaction.atomic()
    def handle(self, *args, **參數):
        for 語料 in (
            語料表.objects
            .filter(校對者__isnull=True)
            .filter(音檔__聲音檔名='LTS30.wav')
        ):
            _原始口語調臺羅, 漢字, 本調, 口語調臺羅 = self.原始通用得著臺羅漢字(語料.頭一版通用)
            print(漢字, 本調, 口語調臺羅)
            語料.漢字 = 漢字
            語料.本調臺羅 = 本調
            語料.口語調臺羅 = 口語調臺羅
            語料.save()
