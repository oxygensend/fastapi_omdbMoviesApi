import re
import pytest
from ..service.CalculationService import CalculationService

def test_calculate_mean():
    body = { 
        'fields': [{'test1': 1 }, 
            {'test2': 2},
            {'test1': 3},
            {'test2': 2}],
        'method': 'mean'
    }

    result = CalculationService.computeStatistics(body)

    assert isinstance(result, dict)
    assert 'test1' in result
    assert 'test2' in result
    assert result['test1'] == 2
    assert result['test2'] == 1.5