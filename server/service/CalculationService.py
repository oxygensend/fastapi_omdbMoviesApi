

from email.policy import default
import numbers
from statistics import mean, median, mode, quantiles, stdev
from unicodedata import numeric

import numpy as np
import main
from py import std

from collections import defaultdict

class CalculationService:

    @classmethod
    def computeStatistics(cls, methods: list, data: list):
        
        allowedMethods = {
            'mean': np.mean,
            'median': np.median,
            'std': stdev,
            'mode': mode,
            'quantile': quantiles,
        }


        try:
            choosenMethods = { method: allowedMethods[method] for method in methods}
        except KeyError:
            return "Provided method is not allowed"

        res = cls._changeDataStructure(data)

        for k,v in res.items():
               if not all(isinstance(x, numbers.Number) for x in v):
                    return "Calculations can be only made on numeric fields"
        return { methodName: {k: round(method(v),2) if methodName != 'quantile' else method(v) for k,v in res.items() } \
                for methodName, method in choosenMethods.items() }
 


    @classmethod
    def _changeDataStructure(cls,data: list) -> dict:
        res = defaultdict(list)
        for d in data:
            for k, v in d.items():
                res[k].append(v)
        
        return res
