
from http.client import ResponseNotReady
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware





class AdminMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next) -> Response:

        if not request.user.isAdmin:
            return Response("Access denied.", status_code = 403) 
        
        return await(request)