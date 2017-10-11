from 語料庫.models import 音檔表
from os.path import join
from subprocess import PIPE, Popen
from tempfile import TemporaryDirectory

from django.http.response import HttpResponse


from 臺灣言語工具.系統整合.程式腳本 import 程式腳本


def 傳音檔(request, 音檔編號, 開始時間, 結束時間):
    全部音檔 = 音檔表.objects.get(id=音檔編號).聲音檔()
    語句音檔 = 全部音檔.照秒數切出音檔(float(開始時間), float(結束時間))
    try:
        with TemporaryDirectory() as 資料夾:
            檔名 = join(資料夾, 'audio.wav')
            with open(檔名, 'wb') as 檔案:
                指令 = Popen(['sox', '-', 檔名, 'remix', '1'], stdin=PIPE)
                指令.communicate(input=語句音檔.wav格式資料())
            程式腳本._走指令(['normalize-audio', 檔名])
            with open(檔名, 'rb') as 檔案:
                資料 = 檔案.read()
    except:
        資料 = 語句音檔.wav格式資料()
    return HttpResponse(
        資料,
        content_type="audio/wav"
    )
