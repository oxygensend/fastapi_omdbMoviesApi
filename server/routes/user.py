from asyncio.log import logger
from distutils.log import error, info
import sys
from urllib import response
sys.path.append("..") # Adds higher directory to python modules path.
from datetime import date, datetime
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


import main
from ..crud.UserCrud import UserCrud
from ..models.User import AuthSchema, UserSchema, UserUpdateSchema, hashPassword
from ..models.Response import Response

router = APIRouter()

@router.post("/", response_description="User added into the database")
async def addUser(user: UserSchema = Body(...)) -> dict:
    user = jsonable_encoder(user)
    user['password'] = hashPassword(user['password']);
    new_user = await UserCrud.add(user)
    main.logger.info(new_user)
    main.logger.info(user)
    return Response.json(new_user, 201)

@router.get("/", response_description="Users retrived from database")
async def getUsers() -> dict:
    users = await UserCrud.retriveAll()
    return Response.json(users)

@router.delete("/{id}",response_description="Delete user")
async def deleteUser(id: str) -> dict:
    return  Response.json(f"User {id} has been removed", 204) \
            if await UserCrud.delete(id) else \
            Response.error("Page not found", f"User with id: {id} doesn't exist", 404)
    
@router.patch('/{id}', response_description="Update user")
async def updateUser(id:str, data: UserUpdateSchema = Body(...)) -> dict:
    data = dict(filter(lambda value: value[1] is not None, data.dict().items()))

    if 'password' in data:
        data['password'] = hashPassword(data['password'])

    main.logger.info(data)
    return Response.json(F"User {id} has been updated", 204) \
        if  await UserCrud.update(id, data) else \
        Response.error("Page not found", f"User with id: {id} doesn't exist", 404)

