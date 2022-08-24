from collections import defaultdict
from http.client import UNAUTHORIZED
from lib2to3.pgen2.token import tok_name
from re import M
import re
import jwt
import main
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from server.middlewares.AbstractMiddleware import AbstractMiddleware

from server.models.User import UserSchema
from ..secret import SECRET_KEY
from ..models.Response import Response as Res


class AuthMiddleware(AbstractMiddleware):

    AUTHORIZED_URLS = defaultdict(list,{
        'POST': ['\/api\/movie'],
        'GET': ['\/api\/movie','\/api\/users'],
        'DELETE': ['\/api\/users'],
        'PATCH': ['\/api\/movies', '\/api\/users']
    })

    async def dispatch(self, request: Request, call_next) -> Response:

      
        if self._checkValidUrl(request):
            return await call_next(request)

        token = request.headers.get('X-Authorization')
        if not token:
            return Response("Authorization required, please login first.", status_code = 401) 

        try:
            token =  jwt.decode(request.headers.get('X-Authorization'), SECRET_KEY, ["HS256"])
            request.state.user = token
        except jwt.ExpiredSignatureError:
            return Response("Token has expired, please refresh.", 400)
        except:
            return Response("Invalid token", 400)


        return await call_next(request)
    