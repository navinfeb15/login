
from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
import schemas, models, database
from . import token
from hashing import Hash
# from .token import create_access_token 
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(),  db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid username')

    if not request.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Password')
    


    access_token = token. create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

