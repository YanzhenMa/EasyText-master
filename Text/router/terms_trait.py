from fastapi import APIRouter
from Text import schema
from Text.base_trait import terms

terms_api = APIRouter(
    prefix="/terms",
    tags=["词特征分析"],
    responses={404: {"description": "operation failed"}}
)


@terms_api.post("/count/")
def count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[统计词数]

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.count(textbase.text, allow_repeat)
    return res


@terms_api.post("/frequency/")
def frequency(textbase: schema.TextBase):
    """[词频1] 分词后的词数/词种数
    """
    res = terms.frequency(textbase.text)
    return res


@terms_api.post("/frequency_sql/")
def frequency_sql(textbase: schema.TextBase):
    """[词频2] 分词后的词数在数据库的频率和/词种数
    """
    res = terms.frequency_sql(textbase.text)
    return res


@terms_api.post("/avg_terms_len/")
def avg_terms_len(textbase: schema.TextBase):
    """[平均词长] 文本字数（不包括文本中的空格但包括标点符号）/文本中的总词数
    """
    res = terms.avg_terms_len(textbase.text)
    return res


@terms_api.post("/difficult_count/")
def difficult_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[难词数] 满足词库中acc_pinlv >= 75 的词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.difficult_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/difficult_ratio/")
def difficult_ratio(textbase: schema.TextBase, allow_repeat: bool = True):
    """[难词比例] 难词数/词总数(不去重)

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.difficult_ratio(textbase.text, allow_repeat)
    return res


@terms_api.post("/noun_count/")
def noun_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[名词数] 词性满足名词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.noun_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/verb_count/")
def verb_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[动词数] 词性满足动词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.verb_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/adj_count/")
def adj_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[形容词数] 词性满足形容词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.adj_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/num_count/")
def num_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[数词数] 词性满足数词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.num_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/quantifier_count/")
def quantifier_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[量词数] 词性满足量词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.quantifier_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/pronoun_count/")
def pronoun_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[代词数] 词性满足代词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.pronoun_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/reality_count/")
def reality_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[实词数] =名词、动词、形容词、数词、量词、代词这六个词的和

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.reality_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/preposition_count/")
def preposition_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[介词数] 词性满足介词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.preposition_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/conjunction_count/")
def conjunction_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[连词数] 词性满足连词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.conjunction_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/particle_count/")
def particle_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[助词数] 词性满足助词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.particle_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/interjection_count/")
def interjection_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[叹词数] 词性满足叹词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.interjection_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/modal_count/")
def modal_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[语气词数] 词性满足语气词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.modal_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/time_count/")
def time_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[时间词数] 词性满足时间词的所有词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.time_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/fictitious_count/")
def fictitious_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[虚词数] =介词、连词、助词、叹词、语气词这五个词的和

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.fictitious_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/reality_ratio_count/")
def reality_ratio_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[实词所占比例] =实词/总词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.reality_ratio_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/fictitious_ratio_count/")
def fictitious_ratio_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[虚词所占比例] =虚词/总词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.fictitious_ratio_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/avg_noun_modifier_count/")
def avg_noun_modifier_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[平均名词修饰语数量] = 名词修饰语数量/总词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.avg_noun_modifier_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/avg_predicate_modifier_count/")
def avg_predicate_modifier_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[平均谓语修饰语数量] = 谓语修饰语数量/总词数

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.avg_predicate_modifier_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/one_level_terms_count/")
def one_level_terms_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[一级词数量] = 查询sql里满足一级词的

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.one_level_terms_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/two_level_terms_count/")
def two_level_terms_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[二级词数量] = 查询sql里满足二级词的

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.two_level_terms_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/three_level_terms_count/")
def three_level_terms_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[三级词数量] = 查询sql里满足三级词的

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.three_level_terms_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/four_level_terms_count/")
def four_level_terms_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[四级词数量] = 查询sql里满足四级词的

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.four_level_terms_count(textbase.text, allow_repeat)
    return res


@terms_api.post("/five_level_terms_count/")
def five_level_terms_count(textbase: schema.TextBase, allow_repeat: bool = True):
    """[五级词数量] = 查询sql里满足五级词的

    Args:

        allow_repeat : 是否去掉重复的字，默认不去重
    """
    res = terms.five_level_terms_count(textbase.text, allow_repeat)
    return res
