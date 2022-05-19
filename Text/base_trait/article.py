"""
文章特征分析

"""
from collections import Counter
from typing import List

from Text.config import settings
from Text.nlp import nlp
from Text.utils import get_std, matrix_to_list


def get_onespeech_terms(text: str, onespeech: str) -> List[List[str]]:
    """[summary]

    Args:
        text (str): [文本]
        onespeech (str): [词性] 暂支持名词和实词

    Returns:
        List[List[str]]: 符合某一词性的所有词组成的嵌套列表
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.split(text)
    if onespeech == 'noun':
        res = [[i[0] for i in nlp.tag(
            text) if i[1] in settings.NOUN_WORDS] for text in result]
    elif onespeech == 'reality':
        res = [[i[0] for i in nlp.tag(
            text) if i[1] in settings.REALITY_WORDS] for text in result]
    else:
        # todo 如果还有别的词性需求
        pass
    return res


def adjacent_sentence_noun_overlap_avg(text: str) -> float:
    """[相邻句子名词重叠平均数] 先取出句子里的所有名词，如果该名词在它相邻的句子里面加将其拿出，最后用拿出来的名词数除以(句子数-1)
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    noun_words = get_onespeech_terms(text, 'noun')
    if len(noun_words) <= 1:
        return 0
    # 判断某一词是否在相邻的下一句里面
    adjacent_overlap_noun = [[word for word in noun_words[i]
                              if word in noun_words[i+1]] for i in range(len(noun_words)-1)]
    return round(len(matrix_to_list(adjacent_overlap_noun))/(len(adjacent_overlap_noun)), 4)


def adjacent_sentence_noun_overlap_std(text: str) -> float:
    """[相邻句子名词重叠标准差] 求名词重叠次数的标准差
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    noun_words = get_onespeech_terms(text, 'noun')
    if len(noun_words) <= 1:
        return 0
    # 判断某一词是否在相邻的下一句里面
    adjacent_overlap_noun = [len([word for word in noun_words[i]
                                  if word in noun_words[i+1]]) for i in range(len(noun_words)-1)]
    # 求列表标准差
    res = get_std(adjacent_overlap_noun)
    return res


def all_sentence_noun_overlap_avg(text: str) -> float:
    """[所有句子名词重叠平均数] 先取出句子里的所有名词，如果该名词在其他句子里面出现就+1，最后用拿出来的名词数除以所有句子数
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    noun_words = get_onespeech_terms(text, 'noun')
    if len(noun_words) <= 1:
        return 0
    # 判断某一词是否在其他句子里面
    all_overlap_noun = [[matrix_to_list(noun_words[i+1::]).count(j)
                         for j in noun_words[i]] for i in range(len(noun_words))]
    # 将二维列表转一维列表
    dimension_all_overlap_noun = matrix_to_list(all_overlap_noun)
    return round(sum(dimension_all_overlap_noun)/len(noun_words), 4)


def all_sentence_noun_overlap_std(text: str) -> float:
    """[所有句子名词重叠标准差] 求所有名词重叠次数的标准差
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    noun_words = get_onespeech_terms(text, 'noun')
    if len(noun_words) <= 1:
        return 0
    # 判断某一词是否在其他句子里面
    all_overlap_noun = [[matrix_to_list(noun_words[i+1::]).count(j)
                         for j in noun_words[i]] for i in range(len(noun_words))]
    # 将二维列表转一维列表
    dimension_all_overlap_noun = matrix_to_list(all_overlap_noun)
    # 求一维列表的标准差
    res = get_std(dimension_all_overlap_noun)
    return res


def adjacent_sentence_reality_overlap_avg(text: str) -> float:
    """[相邻句子实词重叠平均数] 先取出句子里的所有实词，如果该名词在它相邻的句子里面加将其拿出，最后用拿出来的名词数除以(句子数-1)
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    reality_words = get_onespeech_terms(text, 'reality')
    if len(reality_words) <= 1:
        return 0
    # 判断某一词是否在相邻的下一句里面
    adjacent_overlap_reality = [[word for word in reality_words[i]
                                 if word in reality_words[i+1]] for i in range(len(reality_words)-1)]
    return round(len(matrix_to_list(adjacent_overlap_reality))/(len(adjacent_overlap_reality)), 4)


def adjacent_sentence_reality_overlap_std(text: str) -> float:
    """[相邻句子实词重叠标准差] 求实词重叠次数的标准差
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    reality_words = get_onespeech_terms(text, 'reality')
    if len(reality_words) <= 1:
        return 0
    # 判断某一词是否在相邻的下一句里面
    adjacent_overlap_reality = [len([word for word in reality_words[i]
                                     if word in reality_words[i+1]]) for i in range(len(reality_words)-1)]
    # 求列表标准差
    res = get_std(adjacent_overlap_reality)
    return res


def all_sentence_reality_overlap_avg(text: str) -> float:
    """[所有句子实词重叠平均数] 先取出句子里的所有实词，如果该名词在其他句子里面出现就+1，最后用拿出来的名词数除以所有句子数
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    reality_words = get_onespeech_terms(text, 'reality')
    if len(reality_words) <= 1:
        return 0
    # 判断某一词是否在其他句子里面
    all_overlap_reality = [[matrix_to_list(reality_words[i+1::]).count(j)
                            for j in reality_words[i]] for i in range(len(reality_words))]
    # 将二维列表转一维列表
    dimension_all_overlap_reality = matrix_to_list(all_overlap_reality)
    return round(sum(dimension_all_overlap_reality)/len(reality_words), 4)


def all_sentence_reality_overlap_std(text: str) -> float:
    """[所有句子实词重叠标准差] 求所有实词重叠次数的标准差
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    reality_words = get_onespeech_terms(text, 'reality')
    if len(reality_words) <= 1:
        return 0
    # 判断某一词是否在其他句子里面
    all_overlap_reality = [[matrix_to_list(reality_words[i+1::]).count(j)
                            for j in reality_words[i]] for i in range(len(reality_words))]
    # 将二维列表转一维列表
    dimension_all_overlap_reality = matrix_to_list(all_overlap_reality)
    # 求一维列表的标准差
    res = get_std(dimension_all_overlap_reality)
    return res


def adjacent_sentence_similarity_avg(text: str) -> float:
    """[相邻句子相似度的平均数]
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    # 先分句
    result = nlp.split(text)
    if len(result) <= 1:
        similarity = 0
        return similarity
    else:
        similarity_list = []
        for i in range(len(result)-1):
            similarity_result = nlp.text_similarity(result[i], result[i+1])
            similarity_data = similarity_result[0].get('similarity')
            similarity_list.append(similarity_data)
        return round(sum(similarity_list)/len(similarity_list), 4)


def adjacent_sentence_similarity_std(text: str) -> float:
    """[相邻句子相似度的标准差]
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    # 先分句
    result = nlp.split(text)
    if len(result) <= 1:
        similarity = 0
        return similarity
    else:
        similarity_list = []
        for i in range(len(result)-1):
            similarity_result = nlp.text_similarity(result[i], result[i+1])
            similarity_data = similarity_result[0].get('similarity')
            similarity_list.append(similarity_data)
        res = get_std(similarity_list)
        return res


def all_sentence_similarity_avg(text: str) -> float:
    """[所有句子相似度的平均数]
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    # 先分句
    result = nlp.split(text)
    if len(result) <= 1:
        similarity = 0
        return similarity
    else:
        # 如果只有两句话 那就只有相邻
        if len(result) == 2:
            res = adjacent_sentence_similarity_avg(text)
            return res
        similarity_list = []
        for i in range(len(result)-1):
            one_similarity_list = []
            for j in range(i+1, len(result)):
                similarity_result = nlp.text_similarity(result[i], result[j])
                similarity_data = similarity_result[0].get('similarity')
                one_similarity_list.append(similarity_data)
            similarity_list.append(one_similarity_list)
        # 将二维列表转一维列表
        similarity_list = matrix_to_list(similarity_list)
        res = round(sum(similarity_list)/len(result), 4)
        return res


def all_sentence_similarity_std(text: str) -> float:
    """[所有句子相似度的标准差]
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    # 先分句
    result = nlp.split(text)
    if len(result) <= 1:
        similarity = 0
        return similarity
    else:
        # 如果只有两句话 那就只有相邻
        if len(result) == 2:
            res = adjacent_sentence_similarity_std(text)
            return res
        similarity_list = []
        for i in range(len(result)-1):
            one_similarity_list = []
            for j in range(i+1, len(result)):
                similarity_result = nlp.text_similarity(result[i], result[j])
                similarity_data = similarity_result[0].get('similarity')
                one_similarity_list.append(similarity_data)
            similarity_list.append(one_similarity_list)
        # 将二维列表转一维列表
        similarity_list = matrix_to_list(similarity_list)
        # 求标准差
        res = get_std(similarity_list)
        return res


def get_sentiment(text: str):
    '''获取一段话是否积极 判断每句话的态度 积极地数量大于消极的数量则整段话是积极地
    '''
    if not text:
        return '无法计算，请至少输入一句话'
    positive_count = negative_count = 0
    sentiment_analysis = nlp.sentiment_analysis(text)
    attitude_list = []
    for analysi in sentiment_analysis:
        attitude_list.append(analysi.get('label'))
    attitude_dict = Counter(attitude_list)
    positive = attitude_dict.get('positive')
    if positive:
        positive_count = positive
    negative = attitude_dict.get('negative')
    if negative:
        negative_count = negative
    if positive_count > negative_count:
        return 'positive'
    elif positive_count < negative_count:
        return 'negative'
    else:
        return 'neutral'
