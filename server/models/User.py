from datetime import date, datetime
from lib2to3.pgen2.token import OP
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from passlib.context import CryptContext
import jwt
import main


class UserSchema(BaseModel):
    username: str = Field(
        min_length=3, max_length=100, 
    )
    email: EmailStr = Field(
      ...
    )
    password: str = Field(...)
    isAdmin: bool = Field(...)
    createdAt: Optional[datetime] = datetime.now()
    updatedAt: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "username": "Testname",
                "email": "test@test.com",
                "password": "*********",
                "isAdmin": True
            }
        }

class UserUpdateSchema(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    isAdmin: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "username": "Testname",
                "email": "test@test.com",
                "password": "*********",
                "isAdmin": True
                
            }
        }

class AuthSchema(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "test@test.com",
                "password": "*********",
            }
        }

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashPassword(password) -> str :
    return pwd_context.hash(password)

