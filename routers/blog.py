import imp
from ntpath import join
from secrets import choice
import shutil
from fastapi import APIRouter, Depends, UploadFile, File
from routers.schemas import BlogBase, BlogDisplay
from sqlalchemy.orm import Session
from database.database_session import get_db
from database import blog
import string
import random

router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/")
def create_post(request: BlogBase, db: Session = Depends(get_db)):
    return blog.create(db, request)


@router.get("/all")
def get_all_posts(db: Session = Depends(get_db)):
    return blog.list(db)


@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    return blog.delete(id, db)


@router.post("/image")
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_str = "".join(random.choice(letter) for i in range(6))
    suffix = f"_{rand_str}"
    filename = suffix.join(image.filename.rsplit(".", 1))
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}
