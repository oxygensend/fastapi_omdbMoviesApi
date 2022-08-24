from importlib.resources import path
from operator import imod
from tkinter import W
from fastapi import FastAPI
from server.middlewares.AdminMiddleware import AdminMiddleware
from server.middlewares.AuthMiddleware import AuthMiddleware
from server.routes.user import *
from server.routes.auth import *
from server.routes.movie import router as router2
from logging.config import dictConfig
import logging
from server.models.Logger import Logger
from starlette.middleware import Middleware

dictConfig(Logger().dict())
logger = logging.getLogger("movies")
app = FastAPI(middleware=[Middleware(AuthMiddleware), Middleware(AdminMiddleware)])
app.include_router(router, tags=["User"], prefix="/api/users")
app.include_router(router1, tags=["Auth"], prefix="/api")
app.include_router(router2, tags=["Movie"], prefix="/api/movies")


@app.get("/")
async def root():
    return {"message": "Hello World"}