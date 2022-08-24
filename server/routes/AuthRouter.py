from asyncio.log import logger
from distutils.log import error, info
from re import U
import sys
from urllib import response
from ..secret import SECRET_KEY
import jwt
sys.path.append("..") # Adds higher directory to python modules path.
from datetime import date, datetime, timedelta
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder



import main
from ..crud.UserCrud import UserCrud
from ..models.User import AuthSchema, UserSchema, UserUpdateSchema, hashPassword
from ..models.Response import Response
from ..database import user_collection

router1 = APIRouter()
router2 = APIRouter()


@router1.post('/auth', response_description="Get Authentication token")
async def login(data: AuthSchema) -> str :
    data = jsonable_encoder(data)
    user = await user_collection.find_one({"email": data['email']})
    if not user:
        return Response.error("VALIDATION ERRRO","Bad credentials", 400)
    
    user.pop('password', None)
    issuedAt = datetime.now()
    expiredAt = issuedAt + timedelta(minutes = 15)
    user['_id'] = str(user['_id'])
    user['iat'] = issuedAt.timestamp()
    user['exp'] = expiredAt.timestamp()


    encode_data = jwt.encode(payload=user, key=SECRET_KEY);

    return Response.json(encode_data, 200)

