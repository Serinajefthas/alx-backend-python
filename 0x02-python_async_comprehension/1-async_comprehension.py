#!/usr/bin/env python3
"""Module to create async comprehension"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[int]:
    """collects random nums from async generator
    into list then returns the list"""
    results = [i async for i in async_generator()]
    return results
