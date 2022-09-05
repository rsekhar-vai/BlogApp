from fastapi import FastAPI 
from database.db import init_db
from routers import post

app = FastAPI() 
app.include_router(post.router)

init_db()
