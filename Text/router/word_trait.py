from fastapi import APIRouter
from Text import schema
from Text.base_trait import word

word_api = APIRouter(
    prefix="/word",
    tags=["字特征分析"],
    responses={404: {"description": "operation failed"}}
)


@word_api.post("/count/")
def count(textbase: schema.TextBase, allow_repeat: bool = True, in_corpus: bool = True):
    """[统计文本字数]

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
        in_corpus : 是否在语料库里，默认在语料库
    """
    res = word.count(textbase.text, allow_repeat, in_corpus)
    return res


@word_api.post("/frequency/")
def frequency(textbase: schema.TextBase, allow_repeat: bool = True, in_corpus: bool = True):
    """[文本平均字频] 标点符号占分母，不去除

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
        in_corpus : 是否在语料库里，默认在语料库
    """
    res = word.frequency(textbase.text, allow_repeat, in_corpus)
    return res


@word_api.post("/stroke_count/")
def stroke_count(textbase: schema.TextBase, allow_repeat: bool = True, in_corpus: bool = True):
    """[文本平均笔画数] 标点符号占分母，不去除

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
        in_corpus : 是否在语料库里，默认在语料库
    """
    res = word.stroke_count(textbase.text, allow_repeat, in_corpus)
    return res


@word_api.post("/commen_ratio_25/")
def commen_ratio_25(textbase: schema.TextBase, allow_repeat: bool = True, in_corpus: bool = True):
    """[常用字比例1] 标点符号占分母，不去除 统计文本中属于2500字库的比例

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
        in_corpus : 是否在语料库里，默认在语料库
    """
    res = word.commen_ratio_25(textbase.text, allow_repeat, in_corpus)
    return res


@word_api.post("/commen_ratio_35/")
def commen_ratio_35(textbase: schema.TextBase, allow_repeat: bool = True, in_corpus: bool = True):
    """[常用字比例2] 标点符号占分母，不去除 统计文本中属于3500字库的比例

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
        in_corpus : 是否在语料库里，默认在语料库
    """
    res = word.commen_ratio_35(textbase.text, allow_repeat, in_corpus)
    return res


@word_api.post("/commen_ratio_70/")
def commen_ratio_70(textbase: schema.TextBase, allow_repeat: bool = True, in_corpus: bool = True):
    """[通用字比例] 标点符号占分母，不去除 统计文本中属于7000字库的比例

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
        in_corpus : 是否在语料库里，默认在语料库
    """
    res = word.commen_ratio_70(textbase.text, allow_repeat, in_corpus)
    return res
