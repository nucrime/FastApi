from typing import List

from db import schemas, crud
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from .root import get_db

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, database: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(database, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=database, user=user)


@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    users = crud.get_users(database, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, database: Session = Depends(get_db)):
    db_user = crud.get_user(database, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, database: Session = Depends(get_db)
):
    return crud.create_user_item(db=database, item=item, user_id=user_id)
