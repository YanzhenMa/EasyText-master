from fastapi import FastAPI
from Text.router.artitle_trait import article_api
from Text.router.sentence_trait import sentence_api
from Text.router.terms_trait import terms_api
from Text.router.word_trait import word_api
from Text.router.advanced import advanced_api


def register_router(app: FastAPI):
    '''注册子路由
    '''
    app.include_router(word_api)
    app.include_router(terms_api)
    app.include_router(sentence_api)
    app.include_router(article_api)
    app.include_router(advanced_api)
