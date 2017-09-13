from django.test.testcases import TestCase
from 語料庫.models import 音檔表
from 語料庫.管理.校對 import 校對表
from django.template.context import Context
from django.template.base import Template
from django.contrib.auth.models import User


class 校對表標籤試驗(TestCase):

    def setUp(self):
        一音檔 = 音檔表.objects.create(
            類別='戲劇',
            資料夾名='dirsui2',
            聲音檔名='sui2.wav',
            聽拍檔名='sui2.txt',
        )
        一助理 = User.objects.create_user('小豬', 'a@gmail.com', '3333')
        校對表.objects.create(
            校對者=一助理,

            音檔=一音檔,
            聲音結束時間='0',
            聲音開始時間='1',

            語者='sui2',
            頭一版資料='sui2',
            頭一版通用='sui',
            漢字='媠',
            本調臺羅='sui2',
            口語調臺羅='sui2',

            sing5hong5舊編號='333',
            sing5hong5新編號='333',
            sing5hong5有揀出來用無=True,
        )

    def test今仔日校對數量(self):
        rendered = Template(
            '{% load 今仔日校對數量 from gi2_liau7_tags %}'
            '{% 今仔日校對數量 %}'
        ).render(Context())
        self.assertEqual(rendered, "1")

    def test攏總校對數量(self):
        rendered = Template(
            '{% load 攏總校對數量 from gi2_liau7_tags %}'
            '{% 攏總校對數量 %}'
        ).render(Context())
        self.assertEqual(rendered, "1")
