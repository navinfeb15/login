from typing import Optional
from pydantic import BaseModel

class ViewUsers_u(BaseModel):
    email: Optional[str]
    username: Optional[str]

    class Config:
        orm_mode = True

class ViewUsers_a(BaseModel):
    email: str
    username: str
    role: str

    class Config:
        orm_mode = True

class ViewUsers_pr(BaseModel):
    email: str
    username: str
    password : str
    role: str

    class Config:
        orm_mode = True
    
class get_user(BaseModel):
    username: str

    class Config:
        orm_mode = True

class ViewUsers_r(BaseModel):
    role: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: Optional[str] = None


class Login(BaseModel):
    username: str
    password: str

