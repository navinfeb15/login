from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.sql.operators import exists
from oauth2 import get_current_user
import schemas, database, models
from sqlalchemy.orm import Session
from typing import List, Optional
from rolechecker import RoleChecker
from .authorization import user_role
from hashing import Hash

router = APIRouter()

roles2 = ['admin', 'user_l1']
roles1 = ['admin']
allow_resource_a = RoleChecker(roles1)
allow_resource_au = RoleChecker(roles2)

#adding a new user | [Access : Admin,]
@router.post('/add_user', status_code=status.HTTP_201_CREATED, response_model=schemas.ViewUsers_pr, dependencies=[Depends(allow_resource_a)])
def add_user(request: schemas.ViewUsers_pr, db: Session = Depends(database.get_db), current_user: schemas.ViewUsers_a = Depends(get_current_user)):
    try:
        to_add = models.User(email = request.email, username = request.username, password = Hash.bcrypt(request.password), role = request.role)
        db.add(to_add)
        db.commit()
        db.refresh(to_add)
        return to_add
    except Exception:
        return Exception

# Getting specific users | [Access : Admin, user_l1]
@router.get('//{username}', response_model=schemas.ViewUsers_u, dependencies=[Depends(allow_resource_au)])
def get_user(username: str, db: Session = Depends(database.get_db), current_user: schemas.ViewUsers_u = Depends(get_current_user)):
    try:
        cont = db.query(models.User).filter(models.User.username == username).first()
        if not cont:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Users with {username} not found!")
        return cont
    except Exception:
        return Exception

#getting all users with role | [Access : Admin, user_l1]
@router.get('/get_all_users', response_model=List[schemas.ViewUsers_a], dependencies=[Depends(allow_resource_au)])
def user_list(db: Session = Depends(database.get_db), current_user : schemas.ViewUsers_a = Depends(get_current_user)):

    try:
        content = db.query(models.User).all()
        if not content:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Users in Database")
        return content
    except Exception:
        return Exception
     
