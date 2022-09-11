from turtle import title
from routers.schemas import BlogBase, BlogDisplay
from sqlalchemy.orm.session import Session
import datetime
from fastapi import HTTPException, status
from .database_session import Base
from sqlalchemy import Column, Integer, String, DateTime


class Blog(Base):
    __tablename__ = "Blogs"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    title = Column(String)
    content = Column(String)
    creator = Column(String)
    timestamp = Column(DateTime)


def create(db: Session, request: BlogBase):
    new_post = Blog(
        image_url=request.image_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        timestamp=datetime.datetime.now(),
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


def list(db: Session):
    return db.query(Blog).all()


def delete(id: int, db: Session):
    post = db.query(Blog).filter(Blog.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not find post with id {id}",
        )
    db.delete(post)
    db.commit()
    return "ok"
