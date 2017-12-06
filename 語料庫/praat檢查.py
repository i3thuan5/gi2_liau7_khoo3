

class praat檢查:
    def __init__(self):
        self.錯誤 = []

    def 發生錯誤(self, 錯誤):
        self.錯誤.append(錯誤)

    def 錯誤資訊(self):
        return '\n'.join(self.錯誤)
