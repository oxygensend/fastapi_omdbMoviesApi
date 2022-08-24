from abc import ABC, abstractmethod
from collections import defaultdict
import re
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

class AbstractMiddleware(BaseHTTPMiddleware, ABC):

    AUTHORIZED_URLS = defaultdict(list,{})

    @abstractmethod
    async def dispatch(self, request: Request, call_next) -> Response:
        pass

    def _checkValidUrl(self,request: Request) -> bool:
        url = request.scope['path']
        method = request.method
        ilegal=re.findall(r"(?=("+'|'.join(self.AUTHORIZED_URLS[method])+r"))", url)
        
        return False if ilegal and self.AUTHORIZED_URLS[method] else True