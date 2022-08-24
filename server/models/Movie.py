from datetime import date, datetime
from lib2to3.pgen2.token import OP
import re
from turtle import st
from pydantic import BaseModel, EmailStr, Field, ValidationError, validator
from typing import Optional
from ..database import movies_collection

class MovieSchema(BaseModel):
    title: str = Field(...)
    year: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "testTitle",
                "year": "1233"
            }
        }

    @validator('year')
    def yearValidator(cls, year: str) -> str:
        if not re.compile(r"^(\d){4}$").match(year):
            raise ValueError("Provide valid year")


    @classmethod
    async def exists(cls, v: str) -> EmailStr:
        return True if  await movies_collection.find_one({"title": v}) else False







class StatsSchema(BaseModel):
    fields: list = Field(...)
    methods: list = Field(...)

    class Config:
       schema_extra = {
            "example": {
                "fields": ["abc", "abc"],
                "methods": "[mean]"
            }
        } 