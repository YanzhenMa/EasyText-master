from fastapi import APIRouter
from Text import schema
from Text.base_trait import sentence

sentence_api = APIRouter(
    prefix="/sentence",
    tags=["句子特征分析"],
    responses={404: {"description": "operation failed"}}
)


@sentence_api.post("/count/")
def count(textbase: schema.TextBase):
    """[统计句子数]
    """
    res = sentence.count(textbase.text)
    return res


@sentence_api.post("/avg_sentence_word_count/")
def avg_sentence_word_count(textbase: schema.TextBase, allow_punctuation=True):
    """[平均句子字数] = 整篇文章字数和/总句子数

    Args:

        allow_punctuation : [是否含有标点符号]. 默认含有
    """
    res = sentence.avg_sentence_word_count(textbase.text, allow_punctuation)
    return res


@sentence_api.post("/shortest_sentence_word_count/")
def shortest_sentence_word_count(textbase: schema.TextBase):
    """[最短句子字数]
    """
    res = sentence.shortest_sentence_word_count(textbase.text)
    return res


@sentence_api.post("/longest_sentence_word_count/")
def longest_sentence_word_count(textbase: schema.TextBase):
    """[最长句子字数]
    """
    res = sentence.longest_sentence_word_count(textbase.text)
    return res


@sentence_api.post("/over_hundred_ratio/")
def over_hundred_ratio(textbase: schema.TextBase):
    """[计算超过一百个字的句子的比例] = 超过一百字的句子数量/句子数
    """
    res = sentence.over_hundred_ratio(textbase.text)
    return res


@sentence_api.post("/single_sentence/")
def single_sentence(textbase: schema.TextBase):
    """[计算单句数量]
    """
    res = sentence.single_sentence(textbase.text)
    return res


@sentence_api.post("/single_sentence_ratio/")
def single_sentence_ratio(textbase: schema.TextBase):
    """[计算单句比例]
    """
    res = sentence.single_sentence_ratio(textbase.text)
    return res


@sentence_api.post("/double_sentence/")
def double_sentence(textbase: schema.TextBase):
    """[计算复句数量]
    """
    res = sentence.double_sentence(textbase.text)
    return res


@sentence_api.post("/double_sentence_ratio/")
def double_sentence_ratio(textbase: schema.TextBase):
    """[计算复句比例]
    """
    res = sentence.double_sentence_ratio(textbase.text)
    return res
