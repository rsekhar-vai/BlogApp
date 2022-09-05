from fastapi import APIRouter, Depends
from routers.schemas import PostBase, PostDisplay
from sqlalchemy.orm import Session
from database.db import get_db
from database import db_post

router = APIRouter(
        prefix='/post',
        tags=['post']
        )

@router.post('/')
def create_post(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)
