from importlib.resources import path
from operator import imod
from tkinter import W
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from server.middlewares.AdminMiddleware import AdminMiddleware
from server.middlewares.AuthMiddleware import AuthMiddleware
from server.routes.UserRouter import *
from server.routes.AuthRouter import *
from server.routes.MovieRouter import router as router2
from logging.config import dictConfig
import logging
from server.models.Logger import Logger
from starlette.middleware import Middleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


dictConfig(Logger().dict())
logger = logging.getLogger("movies")
app = FastAPI(middleware=[Middleware(AuthMiddleware), Middleware(AdminMiddleware)])
app.include_router(router, tags=["User"], prefix="/api/users")
app.include_router(router1, tags=["Auth"], prefix="/api")
app.include_router(router2, tags=["Movie"], prefix="/api/movies")


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
   return JSONResponse(
        status_code=400,
        content=jsonable_encoder({"detail": exc.errors()})
    )