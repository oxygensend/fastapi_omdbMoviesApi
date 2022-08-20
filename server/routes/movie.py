from asyncio.log import logger
from distutils.log import error, info
import json
import re
import secrets
import sys
from urllib import request, response

import requests
from server.helpers.MovieParser import MovieParser

from server.models.Movie import MovieSchema
sys.path.append("..") # Adds higher directory to python modules path.
from datetime import date, datetime
from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder

import main
from ..crud.MovieCrud import MovieCrud
from ..models.Response import Response
from ..secret import OMDB_URL, API_KEY
router = APIRouter()


@router.post("", response_description="Movie added to database")
async def addMovie(data: MovieSchema = Body(...)) -> dict:
    data = jsonable_encoder(data)
    url=OMDB_URL + "apikey=" + API_KEY +'&t=' + data['title'].replace(' ', '+') + '&y=' + ( data['year'] if data['year'] else '')
    main.logger.info(url)
    movie =  MovieParser.parse(json.loads(requests.get(url).text));
    main.logger.info(movie)
    newMovie = await MovieCrud.add(movie)
    
    return Response.json(newMovie, 201)

@router.get("", response_description="Movies retrived from database")
async def getMovies(request: Request) -> dict:
    main.logger.info(request.query_params)
    movies = await MovieCrud.retriveAll(request.query_params)
    main.logger.info(movies)
    return Response.json(movies)

@router.get("/{id}", response_description="Movie fetched from database")
async def getMovie(id: str, request: Request) -> dict:
    movie = await MovieCrud.retriveOne(id, request.query_params)
    return Response.json(movie) \
           if movie else \
           Response.error("Page not found", f"Movie with id: {id} doesn't exist", 404)         


@router.delete("/{id}",response_description="Delete movie", )
async def deleteMovie(id: str) -> dict:
    return  Response.json(f"Movie {id} has been removed", 204) \
            if await MovieCrud.delete(id) else \
            Response.error("Page not found", f"Movie with id: {id} doesn't exist", 404)
