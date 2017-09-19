from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 用字.models import 用字表
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
# from 臺灣言語工具.斷詞.語言模型揀集內組 import 語言模型揀集內組
from 臺灣言語工具.解析整理.座標揀集內組 import 座標揀集內組
from 臺灣言語工具.辭典.型音辭典 import 型音辭典
from 校對工具.models import 辭典表
from 臺灣言語工具 import 解析整理


class 工具:

    def __init__(self):
        self.辭典 = 型音辭典(4)
        for 分詞 in 辭典表.全部分詞():
            self.辭典.加詞(
                拆文分析器.分詞詞物件(分詞)
            )

    def 標本調(self, 漢字, 原本臺羅):
        句物件 = 拆文分析器.對齊句物件(
            漢字,
            文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 原本臺羅)
        )
        for 字物件 in 句物件.篩出字物件():
            if not 用字表.有這个字無(字物件):
                字物件.音 = 無音
        結果句物件 = (
            句物件
            .揣詞(拄好長度辭典揣詞, self.辭典)
            .揀(座標揀集內組)
            #             .揀(語言模型揀集內組, self.語言模型)
        )
        for 字物件 in 結果句物件.篩出字物件():
            if 字物件.音 == 無音:
                字物件.音 = 字物件.型
        return 解析整理.羅馬字仕上げ.羅馬字仕上げ.輕聲佮外來語(結果句物件.看音())
