from fastapi import APIRouter, status, Depends, HTTPException
from starlette.responses import Response
import schemas, models, database
from rolechecker import RoleChecker
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

allow_resource = RoleChecker(["user"])


#getting all users | [Access : User]
@router.get('/', response_model=List[schemas.ViewUsers_u], dependencies=[Depends(allow_resource)])
def users(db: Session = Depends(database.get_db)):
    try:
        stor = db.query(models.User).all()
        if not stor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Users in Database")
        return stor
    except Exception:
        return Exception
