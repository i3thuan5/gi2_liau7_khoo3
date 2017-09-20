from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 用字.models import 用字表
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.斷詞.語言模型揀集內組 import 語言模型揀集內組
# from 臺灣言語工具.解析整理.座標揀集內組 import 座標揀集內組
from 臺灣言語工具.辭典.型音辭典 import 型音辭典
from 校對工具.models import 辭典表
from 臺灣言語工具 import 解析整理
from os.path import join
import re
from tempfile import TemporaryDirectory
from 語言模型.models import 語言模型表
from 臺灣言語工具.語言模型.KenLM語言模型訓練 import KenLM語言模型訓練
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型


class 工具:

    def __init__(self):
        self.辭典 = 型音辭典(4)
        for 分詞 in 辭典表.全部分詞():
            self.辭典.加詞(
                拆文分析器.分詞詞物件(分詞)
            )
        with TemporaryDirectory() as 資料夾:
            語句 = join(資料夾, '語句.txt')
            with open(語句, 'w') as 檔案:
                for 分詞 in 語言模型表.全部分詞():
                    print(分詞, file=檔案)
            self.語言模型 = KenLM語言模型(
                KenLM語言模型訓練().訓練(
                    [語句],
                    join(資料夾, '暫存資料夾'),
                    連紲詞長度=3
                )
            )

    def 標本調(self, 漢字, 原本臺羅):
        愛處理的漢字 = re.sub('（[^）]+）', ' X ', 漢字)
        try:
            原本句物件 = 拆文分析器.對齊句物件(
                愛處理的漢字,
                文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原本臺羅)
            )
        except:
            原本句物件 = 拆文分析器.建立句物件(愛處理的漢字)
        for 字物件 in 原本句物件.篩出字物件():
            if 字物件.型 == 'X':
                pass
            elif not 用字表.有這个字無(字物件):
                字物件.舊音 = 字物件.音
                字物件.音 = 無音
        結果句物件 = (
            原本句物件
            .揣詞(拄好長度辭典揣詞, self.辭典)
            #             .揀(座標揀集內組)
            .揀(語言模型揀集內組, self.語言模型)
        )
        for 字物件 in 結果句物件.篩出字物件():
            if 字物件.音 == 無音:
                字物件.音 = 字物件.型
        try:
            return 解析整理.羅馬字仕上げ.羅馬字仕上げ.輕聲佮外來語(結果句物件.看音())
        except:
            return 結果句物件.看音().replace('0', '--').replace(' --', '--')
