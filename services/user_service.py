from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(name=user.name, age=user.age, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db:Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def put_user(db: Session, user_id: int, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.id == user_id).first()
    if existing_user:
        existing_user.name = user.name
        existing_user.age = user.age
        existing_user.email = user.email
        db.commit()
        db.refresh(existing_user)
    return existing_user

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
