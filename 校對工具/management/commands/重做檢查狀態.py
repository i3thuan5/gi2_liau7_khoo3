from django.core.management.base import BaseCommand
from 語料庫.管理.校對 import 校對表


class Command(BaseCommand):

    def handle(self, *args, **參數):
        for 語料 in 校對表.objects.all():
            語料.save()
