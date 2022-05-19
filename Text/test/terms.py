import unittest

from Text.base_trait.terms import (adj_count, avg_noun_modifier_count, avg_predicate_modifier_count, avg_terms_len, conjunction_count, count, difficult_count, difficult_ratio, fictitious_count, fictitious_ratio_count, five_level_terms_count, four_level_terms_count, frequency, frequency_sql, interjection_count, modal_count, noun_count, num_count, one_level_terms_count, particle_count, preposition_count, pronoun_count, quantifier_count, reality_count, reality_ratio_count, three_level_terms_count, time_count, two_level_terms_count, verb_count)


class TermsTest(unittest.TestCase):

    def setUp(self):

        self.text = '''当日新增治愈出院病例36例。累计确诊病例10169例，累计治愈出院病例9762例，无死亡病例。
                    '''
        # 处理空格和换行符
        self.text = self.text.replace(' ', '')
        self.text = self.text.replace('\n', '')

    def test_count1(self):
        """[词数]
        """
        self.assertEqual(
            count(self.text),
            22
        )

    def test_count2(self):
        """[词种数]
        """
        self.assertEqual(
            count(self.text, allow_repeat=False),
            14
        )

    def test_frequency(self):
        """[词频1]
        """
        self.assertEqual(
            frequency(self.text),
            1.5714
        )

    def test_frequency_sql(self):
        """[词频2]
        """
        self.assertEqual(
            frequency_sql(self.text),
            0.0042
        )

    def test_avg_terms_len(self):
        """[平均词长]
        """
        self.assertEqual(
            avg_terms_len(self.text),
            2.14
        )

    def test_difficult_count(self):
        """[难词数]
        """
        self.assertEqual(
            difficult_count(self.text),
            12
        )

    def test_difficult_ratio1(self):
        """[难词比例]
        """
        self.assertEqual(
            difficult_ratio(self.text),
            0.5455
        )

    def test_difficult_ratio2(self):
        """[难词词种比例]
        """
        self.assertEqual(
            difficult_ratio(self.text, allow_repeat=False),
            0.3182
        )

    def test_noun_count(self):
        """[名词数]
        """
        self.assertEqual(
            noun_count(self.text),
            4
        )

    def test_verb_count(self):
        """[动词数]
        """
        self.assertEqual(
            verb_count(self.text),
            10
        )

    def test_adj_count(self):
        """[形容词数]
        """
        self.assertEqual(
            adj_count(self.text),
            0
        )

    def test_num_count(self):
        """[数词数]
        """
        self.assertEqual(
            num_count(self.text),
            3
        )

    def test_quantifier_count(self):
        """[量词数]
        """
        self.assertEqual(
            quantifier_count(self.text),
            0
        )

    def test_pronoun_count(self):
        """[代词数]
        """
        self.assertEqual(
            pronoun_count(self.text),
            0
        )

    def test_reality_count(self):
        """[实词数]
        """
        self.assertEqual(
            reality_count(self.text),
            17
        )

    def test_preposition_count(self):
        """[介词数]
        """
        self.assertEqual(
            preposition_count(self.text),
            0
        )

    def test_conjunction_count(self):
        """[连词数]
        """
        self.assertEqual(
            conjunction_count(self.text),
            0
        )

    def test_particle_count(self):
        """[助词数]
        """
        self.assertEqual(
            particle_count(self.text),
            0
        )

    def test_interjection_count(self):
        """[叹词数]
        """
        self.assertEqual(
            interjection_count(self.text),
            0
        )

    def test_modal_count(self):
        """[语气词数]
        """
        self.assertEqual(
            modal_count(self.text),
            4
        )

    def test_time_count(self):
        """[时序词数]
        """
        self.assertEqual(
            time_count(self.text),
            1
        )

    def test_fictitious_count(self):
        """[虚词数]
        """
        self.assertEqual(
            fictitious_count(self.text),
            4
        )

    def test_reality_ratio_count(self):
        """[实词词种数]
        """
        self.assertEqual(
            reality_count(self.text, allow_repeat=False),
            12
        )

    def test_fictitious_ratio_count(self):
        """[虚词词种数]
        """
        self.assertEqual(
            fictitious_count(self.text, allow_repeat=False),
            2
        )

    def test_reality_ratio_count1(self):
        """[实词比例]
        """
        self.assertEqual(
            reality_ratio_count(self.text),
            0.7727
        )

    def test_reality_ratio_count2(self):
        """[实词词种比例]
        """
        self.assertEqual(
            reality_ratio_count(self.text, allow_repeat=False),
            0.8571
        )

    def test_fictitious_ratio_count1(self):
        """[虚词比例]
        """
        self.assertEqual(
            fictitious_ratio_count(self.text),
            0.1818
        )

    def test_fictitious_ratio_count2(self):
        """[虚词词种比例]
        """
        self.assertEqual(
            fictitious_ratio_count(self.text, allow_repeat=False),
            0.1429
        )

    def test_avg_noun_modifier_count(self):
        """[平均名词修饰语数量]
        """
        self.assertEqual(
            avg_noun_modifier_count(self.text, allow_repeat=False),
            0.3571
        )

    def test_avg_predicate_modifier_count(self):
        """[平均谓语修饰语数量]
        """
        self.assertEqual(
            avg_predicate_modifier_count(self.text, allow_repeat=False),
            0.4286
        )

    def test_one_level_terms_count(self):
        """[一级词数量]
        """
        self.assertEqual(
            one_level_terms_count(self.text),
            0
        )

    def test_two_level_terms_count(self):
        """[二级词数量]
        """
        self.assertEqual(
            two_level_terms_count(self.text),
            0
        )

    def test_three_level_terms_count(self):
        """[三级词数量]
        """
        self.assertEqual(
            three_level_terms_count(self.text),
            1
        )

    def test_four_level_terms_count(self):
        """[四级词数量]
        """
        self.assertEqual(
            four_level_terms_count(self.text),
            0
        )

    def test_five_level_terms_count(self):
        """[五级词数量]
        """
        self.assertEqual(
            five_level_terms_count(self.text),
            14
        )


if __name__ == '__main__':

    unittest.main()
