from asyncio.log import logger
from distutils.log import error, info
import json
import re
import secrets
import sys
from urllib import request, response
from fastapi_pagination import Page, paginate

import requests
from server.helpers.MovieParser import MovieParser
from server.middlewares.AuthMiddleware import AuthMiddleware

from server.models.Movie import  MovieSchema, StatsSchema
from server.service.CalculationService import CalculationService
sys.path.append("..") # Adds higher directory to python modules path.
from datetime import date, datetime
from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRoute
import main
from ..crud.MovieCrud import MovieCrud
from ..models.Response import Response
from ..secret import OMDB_URL, API_KEY
router = APIRouter()


@router.post("", response_description="Movie added to database")
async def addMovie(data: MovieSchema = Body(...)) -> dict:
    data = jsonable_encoder(data)
    url=OMDB_URL + "apikey=" + API_KEY +'&t=' + data['title'].replace(' ', '+') + '&y=' + ( data['year'] if data['year'] else '')
    data = json.loads(requests.get(url).text)
    if 'Error' in data:
        return Response.error("Page not found", "Movie with given title/year doesn't exist in OMDB database", 404)

    movie =  MovieParser.parse(data);
    if await MovieSchema.exists(movie['title']):
            return Response.error("Validation error", "This movie already exists in database", 400)
          
    newMovie = await MovieCrud.add(movie)
    
    return Response.json(newMovie, 201)

@router.get("", response_description="Movies retrived from database")
async def getMovies(request: Request) -> dict:
    movies = await MovieCrud.retriveAll(request.query_params)
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


@router.post('/stats', response_description="Make calculations on movies data")
async def getStats(data: StatsSchema = Body(...)) -> dict:
    data = jsonable_encoder(data)
    movies = await MovieCrud.retriveAll(data)
    result = CalculationService.computeStatistics(data['methods'], movies)
    return  Response.json(result) if isinstance(result,dict) else Response.error("Calculation error", result, 400)
