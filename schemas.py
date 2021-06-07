from typing import Optional
from pydantic import BaseModel

class ViewUsers_au(BaseModel):
    name: str
    username: str

    class Config:
        orm_mode = True


class ViewUsers_a(BaseModel):
    name: str
    username: str
    password: str

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
