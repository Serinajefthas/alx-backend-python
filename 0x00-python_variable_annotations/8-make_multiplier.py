#!/usr/bin/env python3
"""a typed annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """method takes float and  function multiplying arg by itself
    callable is generic type hint indicates that object callable, meaning
    can called as function"""
    def mul_function(mul: float) -> float:
        """returns mul arg squared"""
        return mul * multiplier
    return mul_function
