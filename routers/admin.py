from fastapi import APIRouter, status, Depends, HTTPException
from oauth2 import get_current_user
import schemas, database, models
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(prefix="/admin",tags=["Admin"])

#getting all users with password
@router.get('/', response_model=List[schemas.ViewUsers_a])
def user_list(db: Session = Depends(database.get_db), current_user : schemas.ViewUsers_a = Depends(get_current_user)):
    content = db.query(models.User).all()
    if not content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Users in Database")
    return content

#adding a new user


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ViewUsers_au)
def add_user(request: schemas.ViewUsers_a, db: Session = Depends(database.get_db), current_user: schemas.ViewUsers_a = Depends(get_current_user)):
    to_add = models.User(name = request.name, username = request.username, password = request.password)
    db.add(to_add)
    db.commit()
    db.refresh(to_add)
    return to_add
