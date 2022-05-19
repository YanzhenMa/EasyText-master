import unittest

from Text.base_trait.word import (avg_formation, commen_ratio_25, commen_ratio_35, commen_ratio_70, count, frequency, stroke_count)


class WordTest(unittest.TestCase):

    def setUp(self):

        self.text = "11月26日，显示，哈哈哈哈哈。出尔反尔，干涸手镯"
        # 处理空格和换行符
        self.text = self.text.replace(' ', '')
        self.text = self.text.replace('\n', '')

    def test_count1(self):
        '''字数
        '''
        self.assertEqual(
            count(self.text),
            21
        )

    def test_count2(self):
        '''字种
        '''
        self.assertEqual(
            count(self.text, allow_repeat=False),
            14
        )

    def test_frequency_1(self):
        '''字频1
        '''
        self.assertEqual(
            frequency(self.text),
            0.0566
        )

    def test_frequency_2(self):
        '''字频2
        '''
        self.assertEqual(
            frequency(self.text, allow_repeat=False),
            0.0774
        )

    def test_stroke_count1(self):
        '''笔画1
        '''
        self.assertEqual(
            stroke_count(self.text),
            5.81
        )

    def test_stroke_count2(self):
        '''笔画2
        '''
        self.assertEqual(
            stroke_count(self.text, allow_repeat=False),
            5.79
        )

    def test_commen_ratio_25(self):
        '''常用字比例2500
        '''
        self.assertEqual(
            commen_ratio_25(self.text),
            0.62
        )

    def test_commen_specie_25(self):
        '''常用字种2500
        '''
        self.assertEqual(
            commen_ratio_25(self.text, allow_repeat=False),
            0.64
        )

    def test_commen_ratio_35(self):
        '''常用字比例3500
        '''
        self.assertEqual(
            commen_ratio_35(self.text),
            0.71
        )

    def test_commen_specie_35(self):
        '''常用字种3500
        '''
        self.assertEqual(
            commen_ratio_35(self.text, allow_repeat=False),
            0.71
        )

    def test_commen_ratio_70(self):
        '''通用字比例7000
        '''
        self.assertEqual(
            commen_ratio_70(self.text),
            0.81)

    def test_commen_specie_70(self):
        '''通用字种7000
        '''
        self.assertEqual(
            commen_ratio_70(self.text, allow_repeat=False),
            0.86
        )

    def test_avg_formation(self):
        '''平均构词能力
        '''
        self.assertEqual(
            avg_formation(self.text),
            38.99
        )


if __name__ == '__main__':

    unittest.main()
