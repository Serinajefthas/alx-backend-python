#!/usr/bin/env python3
"""a typed annotated function"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """function is passed list and returns tuple with the string
    and the length of that string"""
    return [(i, len(i)) for i in lst]
