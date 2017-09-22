from os.path import join
from tempfile import TemporaryDirectory
from unittest.case import TestCase

from django.core.management import call_command


from 口語辭典.原始通用處理 import 原始通用


class 試驗(TestCase):
    def test_通用轉口語調臺羅(self):
        原本 = 'ho3-lang2-zin2-gam1-sim1-'
        口語調臺羅 = (
            原始通用.通用處理做口語調臺羅(原本)
            .看型(物件分字符號='-')
        )
        self.assertEqual(口語調臺羅, 'hoo3-lang7-tsin7-kam1-sim1')
