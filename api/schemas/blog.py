from pydantic import BaseModel
from typing import Optional
from datetime import date

class ORMBase(BaseModel):
    from_attribute = True


class BlogRecord(ORMBase):
    title: str
    body: str


class BlogCreate(BlogRecord):
    pass

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None

class Blogs(ORMBase):
    id: int
    created_at: date
    

# class ShowBlog(BaseModel):
#     title: str
#     body: str
#     # author: list["ShowUser"] = []
#     class Config:
#         from_attributes = True