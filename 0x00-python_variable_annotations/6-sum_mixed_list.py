#!/usr/bin/env python3
"""a typed annotated function"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Method takes mixed list and returns sum as float"""
    return sum(mxd_lst)
