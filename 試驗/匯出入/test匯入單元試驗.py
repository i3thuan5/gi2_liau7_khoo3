from django.test.testcases import TestCase
from 語料庫.management.commands.匯入1版trs語料 import Command


class 試驗(TestCase):

    def test免閬過(self):
        self.assertTrue(
            Command.判斷先愛先做無('四十外年的老店矣')
        )

    def test愛閬過(self):
        self.assertFalse(
            Command.判斷先愛先做無('SPN')
        )

    def test文句有別的聲(self):
        self.assertFalse(
            Command.判斷先愛先做無('四十外年的老店矣 SPN')
        )
