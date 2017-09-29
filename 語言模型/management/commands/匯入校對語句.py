from django.core.management.base import BaseCommand
from 語言模型.匯校對 import 匯入校對語料


class Command(BaseCommand):

    def handle(self, *args, **參數):
        匯入校對語料()
