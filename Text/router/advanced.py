from fastapi import APIRouter
from Text import schema
from Text.base_trait import advanced

advanced_api = APIRouter(
    prefix="/advanced",
    tags=["高级使用"],
    responses={404: {"description": "operation failed"}}
)


@advanced_api.post("/text_correction/")
def text_correction(textbase: schema.TextBase):
    """[文本纠错]
    """
    res = advanced.text_correction(textbase.text)
    return res


@advanced_api.post("/dialogue/")
def dialogue(textbase: schema.TextBase):
    """[开放对话]
    """
    res = advanced.dialogue(textbase.text)
    return res
