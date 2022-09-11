from fastapi import FastAPI
from database.database_session import init_db
from routers import blog
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(blog.router)
app.mount("/images", StaticFiles(directory="images"), name="images")

origins = ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
init_db()
