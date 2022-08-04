from operator import imod
from tkinter import W
from fastapi import FastAPI
from server.routes.user import *

app = FastAPI()

app.include_router(router, tags=["User"], prefix="/api/users")


@app.get("/")
async def root():
    return {"message": "Hello World"}