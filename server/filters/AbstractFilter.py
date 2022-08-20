

from abc import ABC, abstractmethod


class AbstractFilter(ABC):

    query = dict()
    fields = dict()


    @abstractmethod
    def build(self, params) -> tuple:
        pass

    @abstractmethod
    def _parseUrl(self, params) -> dict:
        pass