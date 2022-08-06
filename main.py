from operator import imod
from tkinter import W
from fastapi import FastAPI
from server.routes.user import *
from server.routes.auth import *
from logging.config import dictConfig
import logging
from server.models.Logger import Logger

dictConfig(Logger().dict())
logger = logging.getLogger("movies")

app = FastAPI()
app.include_router(router, tags=["User"], prefix="/api/users")
app.include_router(router1, tags=["Auth"], prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello World"}