from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, database
from services import user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=list[schemas.UserResponse])
def get_all_users(db: Session = Depends(database.get_db)):
    return user_service.get_all(db)

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return user_service.create_user(db, user)

@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = user_service.get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(database.get_db)):
    user = user_service.delete_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
