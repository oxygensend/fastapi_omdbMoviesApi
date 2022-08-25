from datetime import date, datetime
from lib2to3.pgen2.token import OP
import re
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from passlib.context import CryptContext
from ..database import user_collection
import main
class UserSchema(BaseModel):
    username: str = Field(
        min_length=3, max_length=100, 
    )
    email: EmailStr = Field(...)
    password: str = Field(...)
    isAdmin: Optional[bool] = False
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

    @validator('password')
    def passwordValidator(cls, v: str) -> str:
        if not re.compile(r'^(\w){8}\w*$').match(v):
            raise ValueError("Password must contain at least 5 characters")

        return v
    
    @classmethod
    async def exists(cls, v: str) -> EmailStr:
        return True if  await user_collection.find_one({"email": v}) else False






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

