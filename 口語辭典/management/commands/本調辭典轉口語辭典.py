from django.core.management.base import BaseCommand
from 語言模型.匯資料 import 匯入教典例句


class Command(BaseCommand):

    def handle(self, *args, **參數):
        匯入教典例句()
