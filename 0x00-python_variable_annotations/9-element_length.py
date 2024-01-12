#!/usr/bin/env python3
"""a typed annotated function"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function is passed list and returns tuple with the string
    and the length of that string"""
    return [(i, len(i)) for i in lst]
