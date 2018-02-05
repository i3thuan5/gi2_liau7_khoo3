import json
from os.path import join
from tempfile import TemporaryDirectory

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test.testcases import TestCase


from 語料庫.models import 音檔表
from 語料庫.管理.校對 import 校對表
import io


class 匯出試驗(TestCase):
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
            漢字="阮小弟的個性乎，較直啦，較衝碰",
            本調臺羅="gun2 sio2-ti7 e5 ko3-sing3--honnh4, khah4 tit8--lah4, khah4 tshong2-pong7",
            口語調臺羅="gun1 sio1-ti7 e7 ko2-sing3 honn3, khah8 tit8 la3, khah8 tshong1-pong7",
            sing5hong5舊編號='333',
            sing5hong5新編號='333',
            sing5hong5有揀出來用無=True,
            愛先做無=True,
        )

    def setUp(self):
        self.一音檔 = self.新增音檔('戲劇', 'dirsui2', 'sui2.wav', 'sui2.txt',)
        self.一助理 = self.新增助理('小豬', 'a@gmail.com', '3333')

    def test今仔日校對數量(self):
        self.新增語料(self.一助理, self.一音檔)
        with TemporaryDirectory() as 資料夾:
            檔名 = join(資料夾, 'twisas.json')
            with io.StringIO() as 資訊:
                call_command('匯出2版語料', '--輸出檔名', 檔名, stdout=資訊)
            with open(檔名) as 檔案:
                資料 = json.load(檔案)
        self.assertEqual(
            資料[0]["聽拍資料"][0]['內容'],
            "gun1 sio1-ti7 e7 ko2-sing3 honn3 , khah8 tit8 la3 , khah8 tshong1-pong7"
        )
