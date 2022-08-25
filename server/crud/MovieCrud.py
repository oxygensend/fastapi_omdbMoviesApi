from bson import ObjectId

from server.filters.MovieFilter import MovieFilter
from .CrudInterface import CrudInterface
from ..helpers.MovieHelper import MovieHelper
from ..database import movies_collection
import main

class MovieCrud(CrudInterface):

    movieHelper = MovieHelper()

    @classmethod
    async def retriveAll(cls, params: dict) ->dict:

        main.logger.info(params)
        if params:
           filter = MovieFilter()
           query, fields =  filter.build(params)
        else:
            query, fields = None, None
        


        return [ cls.movieHelper(movie) async for movie in movies_collection.find(query , fields )]

    @classmethod
    async def retriveOne(cls, id: str, params: dict) -> dict:
        
        if params:
           filter = MovieFilter()
           _ , fields =  filter.build(params)
        else:
            fields = None

        movie = await movies_collection.find_one({"_id": ObjectId(id)}, fields)
        main.logger.info(movie)
        return cls.movieHelper(movie) if movie else None

    @classmethod
    async def add(cls, data: dict) ->dict:
        movie = await movies_collection.insert_one(data)
        new_user = await movies_collection.find_one({"_id": movie.inserted_id})
        return cls.movieHelper(new_user)

    @classmethod
    async def update(cls, id: str,  data: dict) -> bool:
        if len(data) < 1:
            return False
        movie = await movies_collection.find_one({"_id": ObjectId(id)})
        if movie:
            updated_movie = await movies_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            return True if updated_movie else False
        return False

    @classmethod
    async def delete(cls, id: str) -> bool:
        movie = await movies_collection.find_one({"_id": ObjectId(id)})
        if movie:
            await movies_collection.delete_one({"_id": ObjectId(id)})
            return True
        else:
            return False
