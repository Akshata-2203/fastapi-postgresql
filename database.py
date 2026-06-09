from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://postgres:ShAk1222@localhost:5432/userdb"

engine=create_engine(URL_DATABASE)
SessionLocal=sessionmaker(autocommit=False,autoflush=True,bind=engine)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        