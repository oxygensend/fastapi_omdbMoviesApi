

from abc import ABC, abstractmethod
from urllib.parse import parse_qs


class AbstractFilter(ABC):

    query = dict()
    fields = dict()


    @abstractmethod
    def build(self, params) -> tuple:
        pass

    def _parseUrl(self, params) -> dict:
        params = parse_qs(str(params))
        return {k: v[0] for k, v in params.items()}



    def _getFields(self, params) -> None:
        if('fields' in params):
            fields = params['fields'].split(",")
            self.fields = { k:1 for k in fields }

        if not 'id' in self.fields:
            self.fields['_id'] = 0

