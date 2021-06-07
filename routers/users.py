from fastapi import APIRouter, status, Depends, HTTPException
from starlette.responses import Response
import schemas, models, database
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(tags=["User"])

#getting all users
# @router.get("/", response_model=List[schemas.ViewUsers_au])
# def user_list_u(db: Session = Depends(database.get_db)):
#     cont = db.query(models.User).all()
#     if not cont:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Users in Database")
#     return cont

@router.get('/', response_model=List[schemas.ViewUsers_au])
def users(db: Session = Depends(database.get_db)):
    stor = db.query(models.User).all()
    if not stor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Users in Database")
    return stor
