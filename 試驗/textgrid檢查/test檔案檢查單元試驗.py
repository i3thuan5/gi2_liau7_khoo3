from unittest.mock import patch

from django.test.testcases import TestCase

from 語料庫.praat檢查 import praat檢查


class textgrid試驗(TestCase):
    def setUp(self):
        self.檢查 = praat檢查()

    @patch('語料庫.praat檢查.praat檢查.提出聽拍資料')
    def test_愛有speech(self, 提出聽拍資料mock):
        提出聽拍資料mock.side_effect = KeyError
        self.檢查.檢查檔案('MH.TextGrid')
        self.assertIn('Speech', self.檢查.錯誤資訊())

    @patch('語料庫.praat檢查.praat檢查.檢查語者')
    @patch('語料庫.praat檢查.praat檢查.檢查聽拍')
    @patch('語料庫.praat檢查.praat檢查.提出聽拍資料')
    def test_無speech資料就攏免檢查(self, 提出聽拍資料mock, 檢查聽拍mock, 檢查語者mock):
        提出聽拍資料mock.return_value = []
        提出聽拍資料mock.side_effect = KeyError
        self.檢查.檢查檔案('MH.TextGrid')
        檢查聽拍mock.assert_not_called()
        檢查語者mock.assert_not_called()

    @patch('語料庫.praat檢查.praat檢查.提出語者資料')
    @patch('語料庫.praat檢查.praat檢查.提出聽拍資料')
    def test_愛有turns(self, 提出聽拍資料mock, 提出語者資料mock):
        提出語者資料mock.side_effect = KeyError
        self.檢查.檢查檔案('MH.TextGrid')
        self.assertIn('Turns', self.檢查.錯誤資訊())

    @patch('語料庫.praat檢查.praat檢查.檢查語者')
    @patch('語料庫.praat檢查.praat檢查.檢查聽拍')
    @patch('語料庫.praat檢查.praat檢查.提出語者資料')
    @patch('語料庫.praat檢查.praat檢查.提出聽拍資料')
    def test_無turns就免檢查語者時間(self, 提出聽拍資料mock, 提出語者資料mock, 檢查聽拍mock, 檢查語者mock):
        提出聽拍資料mock.return_value = []
        提出語者資料mock.side_effect = KeyError
        self.檢查.檢查檔案('MH.TextGrid')
        檢查聽拍mock.assert_called_once_with([])
        檢查語者mock.assert_not_called()

    @patch('語料庫.praat檢查.praat檢查.檢查語者')
    @patch('語料庫.praat檢查.praat檢查.檢查聽拍')
    @patch('語料庫.praat檢查.praat檢查.提出語者資料')
    @patch('語料庫.praat檢查.praat檢查.提出聽拍資料')
    def test_攏正常(self, 提出聽拍資料mock, 提出語者資料mock, 檢查聽拍mock, 檢查語者mock):
        提出聽拍資料mock.return_value = []
        提出語者資料mock.return_value = []
        self.檢查.檢查檔案('MH.TextGrid')
        檢查聽拍mock.assert_called_once_with([])
        檢查語者mock.assert_called_once_with([], [])
