from pydantic import BaseModel


class TextBase(BaseModel):
    text: str
