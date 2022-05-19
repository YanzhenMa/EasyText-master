"""
词特征分析

"""


from Text.config import settings
from Text.model import Ci, Ci_Lv, session
from Text.nlp import nlp
from Text.utils import matrix_to_list


def count(text: str, allow_repeat: bool = True) -> int:
    """词数

    Args:
        text (str): 文本
        allow_repeat (bool, optional): 是否去掉重复的字，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.seg(text)
    terms_list = matrix_to_list(result)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    return len(terms_list)


def frequency(text: str) -> float:
    """词频1 分词后的词数/词种数

    Args:
        text (str): 文本
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_count = count(text)
    terms_specie_count = count(text, allow_repeat=False)
    return round(terms_count / terms_specie_count, 4)


def frequency_sql(text: str) -> float:
    """词频2 分词后的词数在数据库的频率和/词种数 # ? 存疑:为什么不是除以词数

    Args:
        text (str): 文本
        terms_list: [('当日', 'TIME'), ('新增', 'v'), ('治愈', 'v')]
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    fre_sum = 0
    # ?  查询频率 首先看是否满足name和cat都一致，再查询满足name的，查询失败为0
    for terms in terms_list:
        name, cat = terms[0], terms[1]
        qr = session.query(Ci).filter_by(name=name, cat=cat).first()
        if qr is not None:
            fre_sum += qr.pinlv
        else:
            qr = session.query(Ci).filter_by(name=name).first()
            if qr is not None:
                fre_sum += qr.pinlv
    # 词种数
    terms_specie_count = count(text, allow_repeat=False)
    return round(fre_sum / terms_specie_count, 4)


def avg_terms_len(text: str) -> float:
    """[平均词长] 文本字数（不包括文本中的空格但包括标点符号）/文本中的总词数

    Args:
        text (str): [文本]
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_count = count(text)
    # 处理空格和换行符
    text = text.replace(' ', '')
    text = text.replace('\n', '')
    word_count = len(text)
    return round(word_count/terms_count, 2)


def difficult_count(text: str, allow_repeat: bool = True) -> int:
    """[难词数] 满足词库中acc_pinlv >= 75 的词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    res = []
    # ?  查询频率 首先看是否满足name和cat都一致，再查询满足name的，查询失败为0
    for terms in terms_list:
        name, cat = terms[0], terms[1]
        qr = session.query(Ci).filter_by(name=name, cat=cat).first()
        if qr is not None and qr.acc_pinlv >= 75:
            res.append(name)
        else:
            qr = session.query(Ci).filter_by(name=name).first()
            if qr is not None and qr.acc_pinlv >= 75:
                res.append(name)
    return len(res)


def difficult_ratio(text: str, allow_repeat: bool = True) -> float:
    """难词比例 难词数/词总数(不去重)

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 难词比例不去重 难词词种比例去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_count = count(text)
    diff_count = difficult_count(text, allow_repeat)
    return round(diff_count/terms_count, 4)


def noun_count(text: str, allow_repeat: bool = True) -> int:
    """[名词数] 词性满足名词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    noun_list = [terms for terms in terms_list if terms[1]
                 in settings.NOUN_WORDS]
    return len(noun_list)


def verb_count(text: str, allow_repeat: bool = True) -> int:
    """[动词数] 词性满足动词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    verb_list = [terms for terms in terms_list if terms[1]
                 in settings.VERB_WORDS]
    return len(verb_list)


def adj_count(text: str, allow_repeat: bool = True) -> int:
    """[形容词数] 词性满足形容词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    adj_list = [terms for terms in terms_list if terms[1]
                in settings.ADJ_WORDS]
    return len(adj_list)


def num_count(text: str, allow_repeat: bool = True) -> int:
    """[数词数] 词性满足数词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    num_list = [terms for terms in terms_list if terms[1]
                in settings.NUM_WORDS]
    return len(num_list)


def quantifier_count(text: str, allow_repeat: bool = True) -> int:
    """[量词数] 词性满足量词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    quantifier_list = [terms for terms in terms_list if terms[1]
                       in settings.QUANTIFIER_WORDS]
    return len(quantifier_list)


def pronoun_count(text: str, allow_repeat: bool = True) -> int:
    """[代词数] 词性满足代词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    pronoun_list = [terms for terms in terms_list if terms[1]
                    in settings.PRONOUN_WORDS]
    return len(pronoun_list)


def reality_count(text: str, allow_repeat: bool = True) -> int:
    """[实词数] =名词、动词、形容词、数词、量词、代词这六个词的和

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    reality_terms_count = sum([noun_count(text, allow_repeat), verb_count(text, allow_repeat), adj_count(
        text, allow_repeat), num_count(text, allow_repeat), quantifier_count(text, allow_repeat), pronoun_count(text, allow_repeat)])
    return reality_terms_count


def preposition_count(text: str, allow_repeat: bool = True) -> int:
    """[介词数] 词性满足介词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    preposition_list = [terms for terms in terms_list if terms[1]
                        in settings.PREPOSITION_WORDS]
    return len(preposition_list)


def conjunction_count(text: str, allow_repeat: bool = True) -> int:
    """[连词数] 词性满足连词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    conjunction_list = [terms for terms in terms_list if terms[1]
                        in settings.CONJUNCTION_WORDS]
    return len(conjunction_list)


def particle_count(text: str, allow_repeat: bool = True) -> int:
    """[助词数] 词性满足助词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    particle_list = [terms for terms in terms_list if terms[1]
                     in settings.PARTICIPANT_WORDS]
    return len(particle_list)


def interjection_count(text: str, allow_repeat: bool = True) -> int:
    """[叹词数] 词性满足叹词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    interjection_list = [terms for terms in terms_list if terms[1]
                         in settings.INTERPOLATION_WORDS]
    return len(interjection_list)


def modal_count(text: str, allow_repeat: bool = True) -> int:
    """[语气词数] 词性满足语气词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    modal_list = [terms for terms in terms_list if terms[1]
                  in settings.MODAL_WORDS]
    return len(modal_list)


def time_count(text: str, allow_repeat: bool = True) -> int:
    """[时间词数] 词性满足时间词的所有词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    terms_list = nlp.tag(text, auto_split=False)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    time_list = [terms for terms in terms_list if terms[1]
                 in settings.TIME_WORDS]
    return len(time_list)


def fictitious_count(text: str, allow_repeat: bool = True) -> int:
    """[虚词数] =介词、连词、助词、叹词、语气词这五个词的和

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    fictitious_terms_count = sum([preposition_count(text, allow_repeat), conjunction_count(
        text, allow_repeat), particle_count(text, allow_repeat), interjection_count(text, allow_repeat), modal_count(text, allow_repeat)])
    return fictitious_terms_count


def reality_ratio_count(text: str, allow_repeat: bool = True) -> int:
    """[实词所占比例] =实词/总词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    reality_terms_count = sum([noun_count(text, allow_repeat), verb_count(text, allow_repeat), adj_count(
        text, allow_repeat), num_count(text, allow_repeat), quantifier_count(text, allow_repeat), pronoun_count(text, allow_repeat)])
    terms_count = count(text, allow_repeat)
    return round(reality_terms_count / terms_count, 4)


def fictitious_ratio_count(text: str, allow_repeat: bool = True) -> int:
    """[虚词所占比例] =虚词/总词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    fictitious_terms_count = sum([preposition_count(text, allow_repeat), conjunction_count(
        text, allow_repeat), particle_count(text, allow_repeat), interjection_count(text, allow_repeat), modal_count(text, allow_repeat)])
    terms_count = count(text, allow_repeat)
    return round(fictitious_terms_count / terms_count, 4)


def avg_noun_modifier_count(text: str, allow_repeat: bool = True) -> int:
    """[平均名词修饰语数量] = 名词修饰语数量/总词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.ddp(text)
    modifier = matrix_to_list([i.get('deprel') for i in result])
    noun_modifier = [i for i in modifier if i in settings.NONU_MODIFIER]
    terms_count = count(text, allow_repeat)
    return round(len(noun_modifier) / terms_count, 4)


def avg_predicate_modifier_count(text: str, allow_repeat: bool = True) -> int:
    """[平均谓语修饰语数量] = 谓语修饰语数量/总词数

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.ddp(text)
    modifier = matrix_to_list([i.get('deprel') for i in result])
    predicate_modifier = [
        i for i in modifier if i in settings.PREDICATE_MODIFIER]
    terms_count = count(text, allow_repeat)
    return round(len(predicate_modifier) / terms_count, 4)


def one_level_terms_count(text: str, allow_repeat: bool = True) -> int:
    """[一级词数量] = 查询sql里满足一级词的

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.seg(text)
    terms_list = matrix_to_list(result)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    num = 0
    for terms in terms_list:
        qr = session.query(Ci_Lv).filter_by(name=terms).first()
        if qr is not None and qr.level == '1':
            num += 1
    return num


def two_level_terms_count(text: str, allow_repeat: bool = True) -> int:
    """[二级词数量] = 查询sql里满足二级词的

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.seg(text)
    terms_list = matrix_to_list(result)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    num = 0
    for terms in terms_list:
        qr = session.query(Ci_Lv).filter_by(name=terms).first()
        if qr is not None and qr.level == '2':
            num += 1
    return num


def three_level_terms_count(text: str, allow_repeat: bool = True) -> int:
    """[三级词数量] = 查询sql里满足三级词的

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.seg(text)
    terms_list = matrix_to_list(result)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    num = 0
    for terms in terms_list:
        qr = session.query(Ci_Lv).filter_by(name=terms).first()
        if qr is not None and qr.level == '3':
            num += 1
    return num


def four_level_terms_count(text: str, allow_repeat: bool = True) -> int:
    """[四级词数量] = 查询sql里满足四级词的

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.seg(text)
    terms_list = matrix_to_list(result)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    num = 0
    for terms in terms_list:
        qr = session.query(Ci_Lv).filter_by(name=terms).first()
        if qr is not None and qr.level == '4':
            num += 1
    return num


def five_level_terms_count(text: str, allow_repeat: bool = True) -> int:
    """[五级词数量] = 查询sql里满足五级词的

    Args:
        text (str): [文本]
        allow_repeat (bool, optional): 是否去掉重复的词，默认不去重
    """
    if not text:
        return '无法计算，请至少输入一句话'
    result = nlp.seg(text)
    terms_list = matrix_to_list(result)
    if not allow_repeat:
        terms_list = list(set(terms_list))
    num = 0
    for terms in terms_list:
        qr = session.query(Ci_Lv).filter_by(name=terms).first()
        if qr is not None and qr.level == '5':
            num += 1
    return num
