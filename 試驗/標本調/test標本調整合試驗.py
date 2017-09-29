from django.test.testcases import TestCase
from 校對工具.views import 工具
from django.core.management import call_command


class 標本調試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('教典匯入本調辭典')
        cls.工具 = 工具()

    def tearDown(self):
        self.assertEqual(
            self.工具.標本調(self.漢字, self.原本本調),
            self.答案本調
        )

    def test查詞典處理(self):
        self.漢字 = '媠'
        self.原本本調 = 'sui3'
        self.答案本調 = 'sui2'

    def test照詞處理(self):
        self.漢字 = '大人'
        self.原本本調 = 'tua7-lan5'
        self.答案本調 = 'tua7-lang5'

    def test無佇辭典內(self):
        self.漢字 = '丞宏'
        self.原本本調 = 'sing5-hong5'
        self.答案本調 = '丞 hong5'

    def test合音(self):
        self.漢字 = '（查某）人'
        self.原本本調 = 'tsa9-lang5'
        self.答案本調 = 'tsa9 lang5'

    def test字數無仝照漢字(self):
        self.漢字 = '已經到'
        self.原本本調 = 'i2-king1'
        self.答案本調 = 'i2-king1 kau3'
