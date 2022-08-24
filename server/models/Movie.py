from datetime import date, datetime
from lib2to3.pgen2.token import OP
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


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