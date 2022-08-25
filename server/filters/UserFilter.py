from collections import defaultdict
from pytest import param
from server.filters.AbstractFilter import AbstractFilter

from server.helpers.MovieHelper import MovieHelper
from ..database import movies_collection
import main
from urllib.parse import  parse_qs

class UserFilter(AbstractFilter):

    
    def _getFields(self, params) -> None:
        if('fields' in params):
            fields = params['fields'].split(",")
            self.fields = { k:1 for k in fields }

    
    def _getQuery(self, params) -> None:

        if('username' in params):
            self.query['username'] = params['username']
        
        if('email' in params):
            self.query['email'] = params['email']
        
        if('admin' in params):
            self.query['isAdmin'] = params['admin']


    def build(self, params: str) -> tuple:
        
        params = self._parseUrl(params)

        self._getFields(params)
        self._getQuery(params)
        
        return (self.query, self.fields)


