"""
句子特征分析

"""
import re

from Text.nlp import nlp


def count(text: str) -> int:
    """[句子数]
    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.split(text)
    return len(result)


def avg_sentence_word_count(text: str, allow_punctuation: bool = True) -> float:
    """[平均句子字数] = 整篇文章字数和/总句子数

    Args:
        text (str): [文本书]
        allow_punctuation (bool, optional): [是否含有标点符号]. 默认含有
    """
    if not text:
        return '无法计算，请至少输入一句话'
    sentence_count = count(text)
    if not allow_punctuation:
        text = re.sub(r'[^\w]', '', text).replace("_", '')
    return round(len(text)/sentence_count, 2)


def shortest_sentence_word_count(text) -> int:
    """[最短句子字数]

    Args:
        text ([type]): [文本]
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.split(text)
    sentence_lenth = [len(i) for i in result]
    return min(sentence_lenth)


def longest_sentence_word_count(text) -> int:
    """[最长句子字数]

    Args:
        text ([type]): [文本]
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.split(text)
    sentence_lenth = [len(i) for i in result]
    return max(sentence_lenth)


def over_hundred_ratio(text) -> float:
    """[计算超过一百个字的句子的比例] = 超过一百字的句子数量/句子数

    Args:
        text ([type]): [文本]
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.split(text)
    sentence_over_hud = [len(i) for i in result if len(i) >= 100]
    sentence_count = count(text)
    return round(len(sentence_over_hud)/sentence_count, 2)


def single_sentence(text) -> int:
    """[单句数量]=总句数减去复句数

    Args:
        text ([type]): [文本]
    """
    if not text:
        return '无法计算，请至少输入一句话'
    double_sentence_count = double_sentence(text)
    sentence_count = count(text)
    single_sentence_count = sentence_count - double_sentence_count
    return single_sentence_count


def single_sentence_ratio(text) -> float:
    """[单句比例]=单句数量/总句数

    Args:
        text ([type]): [文本]
    """
    if not text:
        return '无法计算，请至少输入一句话'
    single_sentence_count = single_sentence(text)
    sentence_count = count(text)
    return round(single_sentence_count/sentence_count, 2)


def double_sentence(text) -> int:
    """[复句数量]

    Args:
        text ([type]): [文本]
    """
    if not text:
        return '无法计算，请至少输入一句话'
    grammar = nlp.ddp(text)
    speech = nlp.tag(text)
    count = 0
    for ln, sent in enumerate(grammar):
        inx = None
        i = 0
        for lm, arc in enumerate(sent.get('deprel')):
            if arc == 'HED':
                if speech[ln][lm][1] == 'v' or speech[ln][lm][1] == 'a':
                    inx = lm
            if arc == 'COO' and sent.get('head')[lm]-1 == inx:
                i = 1
        count += i
    return count


def double_sentence_ratio(text) -> float:
    """[复句比例]=复句数量/总句数

    Args:
        text ([type]): [文本]
    """
    if not text:
        return '无法计算，请至少输入一句话'
    double_sentence_ratio = double_sentence(text)
    sentence_count = count(text)
    return round(double_sentence_ratio/sentence_count, 2)
