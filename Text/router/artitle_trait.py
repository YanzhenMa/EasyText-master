from fastapi import APIRouter
from Text import schema
from Text.base_trait import article

article_api = APIRouter(
    prefix="/article",
    tags=["文章特征分析"],
    responses={404: {"description": "operation failed"}}
)


@article_api.post("/adjacent_sentence_noun_overlap_avg/")
def adjacent_sentence_noun_overlap_avg(textbase: schema.TextBase):
    """[相邻句子名词重叠平均数]
    """
    res = article.adjacent_sentence_noun_overlap_avg(textbase.text)
    return res


@article_api.post("/adjacent_sentence_noun_overlap_std/")
def adjacent_sentence_noun_overlap_std(textbase: schema.TextBase):
    """[相邻句子名词重叠标准差]
    """
    res = article.adjacent_sentence_noun_overlap_std(textbase.text)
    return res


@article_api.post("/all_sentence_noun_overlap_avg/")
def all_sentence_noun_overlap_avg(textbase: schema.TextBase):
    """[所有句子名词重叠平均数]
    """
    res = article.all_sentence_noun_overlap_avg(textbase.text)
    return res


@article_api.post("/all_sentence_noun_overlap_std/")
def all_sentence_noun_overlap_std(textbase: schema.TextBase):
    """[所有句子名词重叠标准差]
    """
    res = article.all_sentence_noun_overlap_std(textbase.text)
    return res


@article_api.post("/adjacent_sentence_reality_overlap_avg/")
def adjacent_sentence_reality_overlap_avg(textbase: schema.TextBase):
    """[相邻句子实词重叠平均数]
    """
    res = article.adjacent_sentence_reality_overlap_avg(textbase.text)
    return res


@article_api.post("/adjacent_sentence_reality_overlap_std/")
def adjacent_sentence_reality_overlap_std(textbase: schema.TextBase):
    """[相邻句子实词重叠标准差]
    """
    res = article.adjacent_sentence_reality_overlap_std(textbase.text)
    return res


@article_api.post("/all_sentence_reality_overlap_avg/")
def all_sentence_reality_overlap_avg(textbase: schema.TextBase):
    """[所有句子实词重叠平均数]
    """
    res = article.all_sentence_reality_overlap_avg(textbase.text)
    return res


@article_api.post("/all_sentence_reality_overlap_std/")
def all_sentence_reality_overlap_std(textbase: schema.TextBase):
    """[所有句子实词重叠标准差]
    """
    res = article.all_sentence_reality_overlap_std(textbase.text)
    return res


@article_api.post("/adjacent_sentence_similarity_avg/")
def adjacent_sentence_similarity_avg(textbase: schema.TextBase):
    """[相邻句子相似度平均数]
    """
    res = article.adjacent_sentence_similarity_avg(textbase.text)
    return res


@article_api.post("/adjacent_sentence_similarity_std/")
def adjacent_sentence_similarity_std(textbase: schema.TextBase):
    """[相邻句子相似度重叠标准差]
    """
    res = article.adjacent_sentence_similarity_std(textbase.text)
    return res


@article_api.post("/all_sentence_similarity_avg/")
def all_sentence_similarity_avg(textbase: schema.TextBase):
    """[所有句子相似度平均数]
    """
    res = article.all_sentence_similarity_avg(textbase.text)
    return res


@article_api.post("/all_sentence_similarity_std/")
def all_sentence_similarity_std(textbase: schema.TextBase):
    """[所有句子相似度重叠标准差]
    """
    res = article.all_sentence_similarity_std(textbase.text)
    return res


@article_api.post("/get_sentiment/")
def get_sentiment(textbase: schema.TextBase):
    """[判断一段话的情感状态]
    """
    res = article.get_sentiment(textbase.text)
    return res
