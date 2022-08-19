from collections import defaultdict
from pytest import param

from server.helpers.MovieHelper import MovieHelper
from ..database import movies_collection
import main
from urllib.parse import  parse_qs

class MovieFilter():

    fields = dict()
    query = dict()

    async def build(self, params: str):
        
        params = parse_qs(str(params))
        params = {k: v[0] for k, v in params.items()}

        main.logger.info(params)


        if('fields' in params):
            fields = params['fields'].split(",")
            self.fields = { k:1 for k in fields }

        if('title' in params):
            self.query['title'] = params['title']
        
        if('year' in params):
            self.query['year'] = params['year']
        
        if('language' in params):
            self.query['language'] = params['language']
        

        main.logger.info(self.fields)
        main.logger.info(self.query)
        return [ str(movie) async for movie in movies_collection.find(self.query, self.fields)] 


