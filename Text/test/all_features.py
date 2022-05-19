# encoding=utf-8
'''所有的特征整合
'''

import re
# import pandas as pd
from Text.base_trait import article, sentence, terms, word


class Features:

    def __init__(self, text):
        # 处理空格和换行符
        self.text = str(text).replace(' ', '')
        self.text = self.text.replace('\n', '')
        # self.text = self.extract_text_word(self.text)

    def extract_text_word(self):
        # 提取某段话里的中文加标点符号
        if type(self.text) == str:
            p1 = re.compile(
                r"[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5/\n]",
                re.S,
            )
            res = re.findall(p1, self.text)
            return "".join(res)
        else:
            return ''

    def get_features(self):
        # 获取所有特征值
        data = {
            '字数': word.count(self.text),
            '字种': word.count(self.text, allow_repeat=False),
            '字频1': word.frequency(self.text),
            '字频2': word.frequency(self.text, allow_repeat=False),
            '笔画1': word.stroke_count(self.text),
            '笔画2': word.stroke_count(self.text, allow_repeat=False),
            '常用字比例2500': word.commen_ratio_25(self.text),
            '常用字种2500': word.commen_ratio_25(self.text, allow_repeat=False),
            '常用字比例3500': word.commen_ratio_35(self.text),
            '常用字种3500': word.commen_ratio_35(self.text, allow_repeat=False),
            '通用字比例7000': word.commen_ratio_70(self.text),
            '通用字种7000': word.commen_ratio_70(self.text, allow_repeat=False),
            '平均构词能力': word.avg_formation(self.text),
            '词数': terms.count(self.text),
            '词种数': terms.count(self.text, allow_repeat=False),
            '词频1': terms.frequency(self.text),
            '词频2': terms.frequency_sql(self.text),
            '平均词长': terms.avg_terms_len(self.text),
            '难词数': terms.difficult_count(self.text),
            '难词比例': terms.difficult_ratio(self.text),
            '难词词种比例': terms.difficult_ratio(self.text, allow_repeat=False),
            '名词数': terms.noun_count(self.text),
            '动词数': terms.verb_count(self.text),
            '形容词数': terms.adj_count(self.text),
            '数词数': terms.num_count(self.text),
            '量词数': terms.quantifier_count(self.text),
            '代词数': terms.pronoun_count(self.text),
            '实词数': terms.reality_count(self.text),
            '介词数': terms.preposition_count(self.text),
            '连词数': terms.conjunction_count(self.text),
            '助词数': terms.particle_count(self.text),
            '叹词数': terms.interjection_count(self.text),
            '语气词数': terms.modal_count(self.text),
            '时序词数': terms.time_count(self.text),
            '虚词数': terms.fictitious_count(self.text),
            '实词词种数': terms.reality_count(self.text, allow_repeat=False),
            '虚词词种数': terms.fictitious_count(self.text, allow_repeat=False),
            '实词比例': terms.reality_ratio_count(self.text),
            '实词词种比例': terms.reality_ratio_count(self.text, allow_repeat=False),
            '虚词比例': terms.fictitious_ratio_count(self.text),
            '虚词词种比例': terms.fictitious_ratio_count(self.text, allow_repeat=False),
            '平均名词修饰语数量': terms.avg_noun_modifier_count(self.text, allow_repeat=False),
            '平均谓语修饰语数量': terms.avg_predicate_modifier_count(self.text, allow_repeat=False),
            '一级词数量': terms.one_level_terms_count(self.text),
            '二级词数量': terms.two_level_terms_count(self.text),
            '三级词数量': terms.three_level_terms_count(self.text),
            '四级词数量': terms.four_level_terms_count(self.text),
            '五级词数量': terms.five_level_terms_count(self.text),
            '句子数': sentence.count(self.text),
            '平均句子字数含标点': sentence.avg_sentence_word_count(self.text),
            '平均句子字数不含标点': sentence.avg_sentence_word_count(self.text, allow_punctuation=False),
            '最短句子字数': sentence.shortest_sentence_word_count(self.text),
            '最长句子字数': sentence.longest_sentence_word_count(self.text),
            '百字句子所占比例': sentence.over_hundred_ratio(self.text),
            '相邻句子名词重叠平均数': article.adjacent_sentence_noun_overlap_avg(self.text),
            '相邻句子名词重叠标准差': article.adjacent_sentence_noun_overlap_std(self.text),
            '所有句子名词重叠平均数': article.all_sentence_noun_overlap_avg(self.text),
            '所有句子名词重叠标准差': article.all_sentence_noun_overlap_std(self.text),
            '相邻句子实词重叠平均数': article.adjacent_sentence_reality_overlap_avg(self.text),
            '相邻句子实词重叠标准差': article.adjacent_sentence_reality_overlap_std(self.text),
            '所有句子实词重叠平均数': article.all_sentence_reality_overlap_avg(self.text),
            '所有句子实词重叠标准差': article.all_sentence_reality_overlap_std(self.text),
        }

        return data


if __name__ == '__main__':
    text = '''当日新增治愈出院病例36例。累计确诊病例10169例，累计治愈出院病例9762例，无死亡病例。
           '''
    obj = Features(text)
    print(obj.get_features())
