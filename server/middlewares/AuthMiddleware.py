from lib2to3.pgen2.token import tok_name
from re import M
import jwt
import main
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from server.models.User import UserSchema
from ..secret import SECRET_KEY
from ..models.Response import Response as Res


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next) -> Response:

        token = request.headers.get('X-Authorization')
        main.logger.info(token)
        if not token:
            return Response("Authorization required, please login first.", status_code = 401) 


        try:
            token =  jwt.decode(request.headers.get('X-Authorization'), SECRET_KEY, ["HS256"])
            main.logger(UserSchema(token))
        except jwt.ExpiredSignatureError:
            return Response("Token has expired, please refresh.", 400)
        except:
            return Response("Invalid token", 400)


        return await call_next(request)