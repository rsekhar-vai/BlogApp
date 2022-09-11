from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

DbSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = DbSession()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(engine)