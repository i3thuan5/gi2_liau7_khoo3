from 語料庫.models import 音檔表
from django.http.response import StreamingHttpResponse


def 傳音檔(request, 音檔編號, 開始時間, 結束時間):
    全部音檔 = 音檔表.objects.get(id=音檔編號).聲音檔()
    語句音檔 = 全部音檔.照秒數切出音檔(float(開始時間), float(結束時間))
    return StreamingHttpResponse(
        [語句音檔.wav格式資料()],
        content_type="audio/wav"
    )
