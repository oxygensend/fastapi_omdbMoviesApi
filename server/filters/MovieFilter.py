from collections import defaultdict
from pytest import param
from server.filters.AbstractFilter import AbstractFilter

from server.helpers.MovieHelper import MovieHelper
from ..database import movies_collection
import main
from urllib.parse import  parse_qs

class MovieFilter(AbstractFilter):

    
    def _getQuery(self, params) -> None:

        if('title' in params):
            self.query['title'] = params['title']
        
        if('year' in params):
            self.query['year'] = params['year']
        
        if('language' in params):
            self.query['language'] = {"$regex": params['language'], "$options": "-i" }
        
        if('genres' in params):
            genres = params['genres'].split(",")
            self.query['genres'] = {"$regex": "|".join(genres), "$options": "-i"}

        if('directors' in params):
            directors = params['directors'].split(",")
            self.query['directors'] = {"$regex": "|".join(directors), "$options": "-i"}

        if("runtime_lt" in params and "runtime_gt" in params):
            self.query['runtime'] = {"$lt": params['runtime_lt'], '$gt': params['runtime_gt']}
        elif("runtime_lt" in params):
            self.query['runtime'] = {"$lt": params['runtime_lt']}
        elif("runtime_gt" in params):
            self.query['runtime'] = {"$gt": params['runtime_gt']}
        
        if("votes_lt" in params and "votes_lt" in params):
            self.query['votes'] = {"$lt": params['votes_lt'], '$gt': params['votes_gt']}
        elif("votes_lt" in params):
            self.query['votes'] = {"$lt": params['votes_lt']}
        elif("votes_gt" in params):
            self.query['votes'] = {"$gt": params['votes_gt']}

        if("rating_lt" in params and "rating_gt" in params):
            self.query['rating'] = {"$lt": params['rating_lt'], '$gt': params['rating_gt']}
        elif("rating_lt" in params):
            self.query['rating'] = {"$lt": params['rating_lt']}
        elif("rating_gt" in params): 
            self.query['rating'] = {"$gt": params['rating_gt']}

        if("metascore_lt" in params and "metascore_gt" in params):
            self.query['metascore'] = {"$lt": params['metascore_lt'], '$gt': params['metascore_gt']}
        elif("metascore_gt" in params):
            self.query['metascore'] = {"$lt": params['metascore_lt']}
        elif("metascore_gt" in params):
            self.query['metascore'] = {"$gt": params['metascore_gt']}

        if("income_lt" in params and "income_gt" in params):
            self.query['income'] = {"$lt": params['income_lt'], '$gt': params['income_gt']}
        elif("income_lt" in params):
            self.query['income'] = {"$lt": params['income_lt']}
        elif("income_gt" in params):
            self.query['income'] = {"$gt": params['income_gt']}




    def build(self, params: str) -> tuple:
        
        if isinstance(params, str):
            params = self._parseUrl(params)

            self._getFields(params)
            self._getQuery(params)
        else:
            self._getFields(params)
        
        return (self.query, self.fields)


