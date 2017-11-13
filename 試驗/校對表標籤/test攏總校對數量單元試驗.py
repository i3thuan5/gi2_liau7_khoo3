from django.test.testcases import TestCase
from 語料庫.models import 音檔表
from 語料庫.管理.校對 import 校對表
from django.template.context import Context
from django.template.base import Template
from django.contrib.auth.models import User


class 攏總校對數量試驗(TestCase):

    def 新增音檔(self, 類別, 資料夾名, 聲音檔名, 聽拍檔名):
        一音檔 = 音檔表.objects.create(
            類別=類別,
            資料夾名=資料夾名,
            聲音檔名=聲音檔名,
            聽拍檔名=聽拍檔名,
        )
        return 一音檔

    def 新增助理(self, 名, 信箱, 密碼):
        一助理 = User.objects.create_user(名, 信箱, 密碼)
        return 一助理

    def 新增語料(self, 校對者, 音檔):
        校對表.objects.create(
            校對者=校對者,
            音檔=音檔,
            聲音結束時間='0',
            聲音開始時間='1',
            漢字='媠',
            本調臺羅='sui2',
            口語調臺羅='sui2',
            sing5hong5舊編號='333',
            sing5hong5新編號='333',
            sing5hong5有揀出來用無=True,
            愛先做無=True,
        )

    def setUp(self):
        self.一音檔 = self.新增音檔('戲劇', 'dirsui2', 'sui2.wav', 'sui2.txt',)
        self.一助理 = self.新增助理('小豬', 'a@gmail.com', '3333')

    def test攏總校對數量(self):
        self.新增語料(self.一助理, self.一音檔)
        rendered = Template(
            '{% load 攏總校對數量 from gi2_liau7_tags %}'
            '{% 攏總校對數量 %}'
        ).render(Context())
        self.assertEqual(rendered, "1")
