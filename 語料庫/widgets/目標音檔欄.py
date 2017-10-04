from django.utils.html import format_html


class 目標音檔欄():

    def 目標音檔(self, obj):
        return format_html('''<audio controls>
        <source src='/音檔/{}/{}/{}/audio.wav'>
        Your browser does not support the audio element.</audio>''',
                           obj.音檔.id, obj.聲音開始時間, obj.聲音結束時間
                           )
