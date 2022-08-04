from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..crud.UserCrud import UserCrud
from ..models.User import (
    ResponseModel,
    UserSchema,
)

router = APIRouter()

@router.post("/", response_description="User added into the database")
async def addStudentData(student: UserSchema = Body(...)):
    student = jsonable_encoder(student)
    new_user = await UserCrud.add(student)
    return ResponseModel(new_user, "User added successfully.", 201)