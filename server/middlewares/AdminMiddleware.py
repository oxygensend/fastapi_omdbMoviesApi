
from collections import defaultdict
from http.client import ResponseNotReady
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from server.middlewares.AbstractMiddleware import AbstractMiddleware




class AdminMiddleware(AbstractMiddleware):


    AUTHORIZED_URLS = defaultdict(list,{
        'DELETE': ['\/api\/users','\/api\/movies'],
        'PATCH': ['\/api\/users','\/api/movies'],
    })

    async def dispatch(self, request: Request, call_next) -> Response:

        if self._checkValidUrl(request):
            return await call_next(request)

        if not request.state.user['isAdmin']:
            return Response("Access denied.", status_code = 403) 
        
        return await call_next(request)