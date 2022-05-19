"""
字特征分析

语料库：现代汉语语料库，截止目前位置共收录20918个字符，含中文标点和全角阿拉伯数字
注意： 涉及到字数的统计，只统计语料库里面收录的字！！！
注意： 涉及到字数的统计，只统计语料库里面收录的字！！！
注意： 涉及到字数的统计，只统计语料库里面收录的字！！！
"""


import numpy as np
from Text.model import Zi, session


def count(text: str, allow_repeat: bool = True, in_corpus: bool = True):
    '''文本字数

    Args:
        text (str): 文本
        allow_repeat (bool, optional): 是否去掉重复的字，默认不去重
        in_corpus (bool, optional): 是否在语料库里，默认在语料库
    '''
    if not text:
        return '无法计算，请至少输入一句话'
    word_list = [w for w in text if w]
    if not allow_repeat:
        word_list = list(set(word_list))
    if not in_corpus:
        return len(word_list)
    query_result = [w for w in word_list if session.query(
        Zi.name).filter_by(name=w).first()]
    return len(query_result)


def frequency(text: str, allow_repeat: bool = True, in_corpus: bool = True):
    '''文本平均字频（标点符号占分母，不去除）

    Args:
        text (str): 文本
        allow_repeat (bool, optional):  是否去掉重复的字，默认不去重
        in_corpus (bool, optional): 是否在语料库里，默认在语料库
    '''
    if not text:
        return '无法计算，请至少输入一句话'
    word_list = [w for w in text if w]
    if not allow_repeat:
        word_list = list(set(word_list))
    word_count = count(text, allow_repeat, in_corpus)
    query_result = []
    for w in word_list:
        qr = session.query(Zi.pinlv).filter_by(name=w).first()
        if qr and qr.pinlv:
            query_result.append(qr)
    sum_hz = np.array(query_result).sum()
    return round(sum_hz / word_count, 4)


def stroke_count(text: str, allow_repeat: bool = True, in_corpus: bool = True):
    '''文本平均笔画数（标点符号占分母，不去除）

    Args:
        text (str): 文本
        allow_repeat (bool, optional): 是否去掉重复的字，默认不去重
        in_corpus (bool, optional): 是否在语料库里，默认在语料库
    '''
    if not text:
        return '无法计算，请至少输入一句话'
    word_list = [w for w in text if w]
    word_count = count(text, allow_repeat, in_corpus)
    if not allow_repeat:
        word_list = list(set(word_list))
    query_result = []
    for w in word_list:
        qr = session.query(Zi.bihua).filter_by(name=w).first()
        if qr and qr.bihua:
            query_result.append(qr)
    sum_stroke_count = np.array(query_result).sum()
    return round(sum_stroke_count / word_count, 2)


def commen_ratio_25(text: str, allow_repeat: bool = True, in_corpus: bool = True):
    '''常用字比例1（标点符号占分母，不去除）统计文本中属于2500字库的比例
    数据库仅有c3500和t7000两个指标 其中常用2500指的是c3500=1 常用3500指的是c3500=1和c3500=2的和
    Args:
        text (str): 文本
        allow_repeat (bool, optional): 是否去掉重复的字，默认不去重
        in_corpus (bool, optional): 是否在语料库里，默认在语料库
    '''
    if not text:
        return '无法计算，请至少输入一句话'
    word_list = [w for w in text if w]
    word_count = count(text, allow_repeat, in_corpus)
    if not allow_repeat:
        word_list = list(set(word_list))
    query_result = []
    for w in word_list:
        qr = session.query(Zi.c3500).filter_by(name=w).first()
        if qr and qr.c3500 == 1:
            query_result.append(qr)
    return round(len(query_result) / word_count, 2)


def commen_ratio_35(text: str, allow_repeat: bool = True, in_corpus: bool = True):
    '''常用字比例2（标点符号占分母，不去除）统计文本中属于3500字库的比例
    数据库仅有c3500和t7000两个指标 其中常用2500指的是c3500=1 常用3500指的是c3500=1和c3500=2的和
    Args:
        text (str): 文本
        allow_repeat (bool, optional): 是否去掉重复的字，默认不去重
        in_corpus (bool, optional): 是否在语料库里，默认在语料库
    '''
    if not text:
        return '无法计算，请至少输入一句话'
    word_list = [w for w in text if w]
    word_count = count(text, allow_repeat, in_corpus)
    if not allow_repeat:
        word_list = list(set(word_list))
    query_result = []
    for w in word_list:
        qr = session.query(Zi.c3500).filter_by(name=w).first()
        if qr and (qr.c3500 == 1 or qr.c3500 == 2):
            query_result.append(qr)
    return round(len(query_result) / word_count, 2)


def commen_ratio_70(text: str, allow_repeat: bool = True, in_corpus: bool = True):
    '''通用字比例（标点符号占分母，不去除）统计文本中属于7000字库的比例
    数据库仅有c3500和t7000两个指标 其中常用2500指的是c3500=1 常用3500指的是c3500=1和c3500=2的和
    Args:
        text (str): 文本
        allow_repeat (bool, optional): 是否去掉重复的字，默认不去重
        in_corpus (bool, optional): 是否在语料库里，默认在语料库
    '''
    if not text:
        return '无法计算，请至少输入一句话'
    word_list = [w for w in text if w]
    word_count = count(text, allow_repeat, in_corpus)
    if not allow_repeat:
        word_list = list(set(word_list))
    query_result = []
    for w in word_list:
        qr = session.query(Zi.t7000).filter_by(name=w).first()
        if qr and qr.t7000 == 1:
            query_result.append(qr)
    return round(len(query_result) / word_count, 2)


def avg_formation(text: str, allow_repeat: bool = True, in_corpus: bool = True):
    ''' 平均构词能力（标点符号占分母，不去除）构词能力之和除以总字数

    Args:
        text (str): 文本
        allow_repeat (bool, optional): 是否去掉重复的字，默认不去重
        in_corpus (bool, optional): 是否在语料库里，默认在语料库
    '''
    if not text:
        return '无法计算，请至少输入一句话'
    word_list = [w for w in text if w]
    word_count = count(text, allow_repeat, in_corpus)
    if not allow_repeat:
        word_list = list(set(word_list))
    query_result = []
    for w in word_list:
        qr = session.query(Zi.gouci).filter_by(name=w).first()
        if qr and qr.gouci:
            query_result.append(qr)
    all_formation = np.array(query_result).sum()
    return round(all_formation / word_count, 2)
