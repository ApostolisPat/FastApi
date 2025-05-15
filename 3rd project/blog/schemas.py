# JSON objects that serve as Request Bodies

from pydantic import BaseModel
class Blog(BaseModel):
    title: str
    body: str