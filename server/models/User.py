from datetime import datetime
from lib2to3.pgen2.token import OP
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserSchema(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    isAdmin: bool = Field(...)
    createdAt: datetime = Field()
    updatedAt: datetime = Field()

    class Config:
        schema_extra = {
            "example": {
                "username": "Testname",
                "email": "test@test.com",
                "password": "*********"
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
                "password": "*********"
            }
        }

def ResponseModel(data, message, code=200):
    return {
        "data": [data],
        "code": code,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
