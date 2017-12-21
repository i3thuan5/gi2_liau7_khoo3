from os.path import dirname, join
from unittest.mock import patch

from django.core.management import call_command
from django.test.testcases import TestCase


from 校對工具.views import 工具
from tempfile import TemporaryDirectory
from os import makedirs


class 試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('教典匯入本調辭典')
        call_command('本調辭典轉口語辭典')
        call_command('匯入教典例句')

    @patch('Pyro4.Proxy')
    def test匯一擺(self, proxyMock):
        proxyMock.return_value = 工具()
        with TemporaryDirectory() as 暫時資料夾:
            音檔資料夾 = join(暫時資料夾, 'Finished')
            LTS資料夾 = join(音檔資料夾, 'LTS')
            makedirs(LTS資料夾)
            with open(join(LTS資料夾, 'LTS30.wav'), 'wb'):
                pass
            call_command(
                '匯入1版TextGrid語料',
                join(dirname(__file__), 'Praat當佇改佮改好的'), 音檔資料夾,
                'LTS',
                'LTS30-1.TextGrid', 'LTS30.wav'
            )
