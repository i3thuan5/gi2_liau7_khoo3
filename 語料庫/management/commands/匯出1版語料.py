
from 語料庫.management.commands.匯出2版語料 import Command as 匯出2版語料Command
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class Command(匯出2版語料Command):
    預設檔名 = 'twisas1.json'

    def 轉做json(self, 資料):
        return {
            "結束時間": 資料.聲音結束時間,
            "開始時間": 資料.聲音開始時間,
            "語者": 資料.語者,
            "漢字": 資料.漢字,
            '本調臺羅': 資料.本調臺羅,
            "口語臺羅": 資料.頭一版轉出來的口語調臺羅,
            "內容": 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 資料.頭一版轉出來的口語調臺羅),
        }
