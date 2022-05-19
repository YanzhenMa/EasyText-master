import unittest
from Text.nlp import nlp


class NlpTest(unittest.TestCase):

    def setUp(self):
        self.text = '''
        当日   新增治愈出院病例36例。
        累计确诊病例10169例，累计治愈出院病例9762例，无死亡病例。
        '''
        # self.text = '''
        # 当日   新增治愈出院病例36例。
        # '''
        self.e_text = '''
        Everyone has talent.
        What is rare is the courage to follow the talent to the dark place where it leads.
        '''
        self.corr_text = '''
        遇到逆竟时，我们必须勇于面对，而且要愈挫愈勇。人生就是如此，经过磨练才能让自己更加拙壮，才能使自己更加乐观。
        '''
        self.question_text = '''
        中国的国土面积有多大？
        '''
        self.poetry_text = '''
        林密不见人
        '''
        self.dialogue_text = ["你好", "吃饭了吗"]

    def test_split(self):
        '''分句
        '''
        result = nlp.split(self.text)
        correct_result = ['当日   新增治愈出院病例36例。',
                          '累计确诊病例10169例，累计治愈出院病例9762例，无死亡病例。']
        self.assertListEqual(result, correct_result)
        correct_e_result = ['Everyone has talent.',
                            'What is rare is the courage to follow the talent to the dark place where it leads.']
        e_result = nlp.split(self.e_text)
        self.assertListEqual(e_result, correct_e_result)

    def test_seg(self):
        '''分词
        '''
        result = nlp.seg(self.text)
        correct_result = [['当日', '新增', '治愈', '出院', '病例', '36例', '。'], [
            '累计', '确诊', '病例', '10169例', '，', '累计', '治愈', '出院', '病例', '9762例', '，', '无', '死亡', '病例', '。']]
        self.assertListEqual(result, correct_result)

    def test_tag(self):
        '''词性标注
        '''
        result = nlp.tag(self.text, auto_split=False)
        correct_result = [('当日', 'TIME'), ('新增', 'v'), ('治愈', 'v'), ('出院', 'vn'), ('病例', 'n'), ('36例', 'm'), ('。', 'w'), ('累计', 'v'), ('确诊', 'v'), ('病例', 'n'), (
            '10169例', 'm'), ('，', 'w'), ('累计', 'vd'), ('治愈', 'v'), ('出院', 'vn'), ('病例', 'n'), ('9762例', 'm'), ('，', 'w'), ('无', 'v'), ('死亡', 'vn'), ('病例', 'n'), ('。', 'w')]
        self.assertListEqual(result, correct_result)

    @unittest.skip
    def test_ner(self):
        '''命名实体识别
        '''
        result = nlp.ner(self.text)
        correct_result = [[('当日', '时间类'), ('   新增', '场景事件'), ('治愈', '场景事件'), ('出院病例', '信息资料'), ('36例', '数量词'), ('。', 'w')], [('累计', '场景事件'), ('确诊病例', '信息资料'), ('10169例', '数量词'),
                                                                                                                             ('，', 'w'), ('累计', '场景事件'), ('治愈', '场景事件'), ('出院病例', '信息资料'), ('9762例', '数量词'), ('，', 'w'), ('无', '否定词'), ('死亡', '场景事件'), ('病例', '信息资料'), ('。', 'w')]]
        self.assertListEqual(result, correct_result)

    def test_ddp(self):
        '''依存句法分析
        '''
        result = nlp.ddp(self.text)
        correct_result = [{'word': ['当日', ' ', ' ', ' ', '新增', '治愈', '出院', '病例', '36例', '。'], 'head': [5, 1, 1, 1, 0, 5, 8, 5, 8, 5], 'deprel': ['ADV', 'MT', 'MT', 'MT', 'HED', 'CMP', 'ATT', 'VOB', 'ATT', 'MT']}, {'word': ['累计', '确诊', '病例', '10169例',
                                                                                                                                                                                                                               '，', '累计', '治愈', '出院', '病例', '9762例', '，', '无', '死亡', '病例', '。'], 'head': [2, 3, 0, 3, 3, 7, 9, 7, 10, 12, 10, 3, 14, 12, 12], 'deprel': ['ADV', 'ATT', 'HED', 'ATT', 'MT', 'ADV', 'ATT', 'CMP', 'SBV', 'VOB', 'MT', 'IC', 'ATT', 'VOB', 'MT']}]
        self.assertListEqual(result, correct_result)

    def test_correcttion(self):
        '''文本纠错
        '''
        result = nlp.text_correction(self.corr_text)
        correct_result = [{'source': '遇到逆竟时，我们必须勇于面对，而且要愈挫愈勇。', 'target': '遇到逆境时，我们必须勇于面对，而且要愈挫愈勇。', 'errors': [{'position': 3, 'correction': {'竟': '境'}}]}, {
            'source': '人生就是如此，经过磨练才能让自己更加拙壮，才能使自己更加乐观。', 'target': '人生就是如此，经过磨练才能让自己更加茁壮，才能使自己更加乐观。', 'errors': [{'position': 18, 'correction': {'拙': '茁'}}]}]
        self.assertListEqual(result, correct_result)

    @unittest.skip
    def test_question_answering(self):
        '''生成式问答
        '''
        result = nlp.question_answering(self.question_text)
        correct_result = [{'text': '中国的国土面积有多大？', 'answer': '960万平方公里。'}]
        self.assertListEqual(result, correct_result)

    @unittest.skip
    def test_poetry(self):
        '''生成式问答
        '''
        result = nlp.poetry(self.poetry_text)
        correct_result = [{'text': '林密不见人', 'answer': ',但闻人语响。'}]
        self.assertListEqual(result, correct_result)

    # @unittest.skip
    def test_dialogue(self):
        '''开放域对话 因为回答是随机的 所以没法equal
        '''
        result = nlp.dialogue(self.dialogue_text)
        print(result)


if __name__ == "__main__":

    unittest.main()
