"""
一些高级使用

"""

from typing import List

from Text.nlp import nlp


def text_correction(text):
    '''文本纠错
    '''
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.text_correction(text)
    if result:
        res = [i.get('target') for i in result]
        return ''.join(res)


def dialogue(text) -> List:
    '''开放对话
    '''
    if not text:
        return '无法计算，请至少输入一句话'
    text = [text]
    result = nlp.dialogue(text)
    return result
