#!/usr/bin/env python3
"""a typed annotated function"""
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Method takes str and int/float and returns tuple"""
    return (k, float(v*v))
