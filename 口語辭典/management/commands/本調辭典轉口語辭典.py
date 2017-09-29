from django.core.management.base import BaseCommand
from 口語辭典.匯資料 import 轉到口語辭典


class Command(BaseCommand):

    def handle(self, *args, **參數):
        轉到口語辭典()
