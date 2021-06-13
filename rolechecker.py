from fastapi import Depends, HTTPException, status
from typing import List
import schemas, oauth2, database, models
from sqlalchemy.orm import Session
from oauth2 import get_current_user


class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, user: schemas.TokenData = Depends(get_current_user), db: Session = Depends(database.get_db)):

        cont = db.query(models.User).filter(models.User.username == user.name).first()

        if cont.role not in self.allowed_roles:
            raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Operation Requests Role Elevation")
        
