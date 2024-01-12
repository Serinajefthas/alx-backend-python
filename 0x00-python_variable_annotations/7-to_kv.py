#!/usr/bin/env python3
"""a typed annotated function"""
from typing import Union, List, Tuple
from numbers import Real


def to_kv(k: str, v: Real) -> Tuple[str, float]:
    """Method takes str and int/float and returns tuple"""
    return k, v * v
