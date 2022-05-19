from fastapi import FastAPI

from Text.register import register_router


app = FastAPI(title='文本特征分析后端', description='此api是文本特征分析后端的所有api集合')


# 注册的顺序不能随意改动，是有意义的，某些注册之间存在依赖关系
register_router(app)
