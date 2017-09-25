from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **參數):
        call_command('校對語句匯口語辭典')
        call_command('匯入校對語句')
        call_command('訓練語言模型')
