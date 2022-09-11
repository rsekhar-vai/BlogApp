from pydantic import BaseModel
from datetime import datetime


class BlogBase(BaseModel):
    image_url: str
    title: str
    content: str
    creator: str


class BlogDisplay(BaseModel):
    id: int
    image_url: str
    title: str
    content: str
    creator: str
    timestamp: datetime

    class Config:
        orm_mode = True
