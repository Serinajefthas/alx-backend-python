#!/usr/bin/env python3
"""a typed annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Method takes list floats and returns sum as a float"""
    return sum(input_list)
