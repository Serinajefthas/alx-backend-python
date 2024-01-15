#!/usr/bin/env python3
"""Module for an asynchronous coroutine function"""
import asyncio
from typing import List
import importlib

wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """creates n wait_random coroutines w max_delay
    and returns list of delays"""
    delay_list = []
    for i in range(n):
        tasks = wait_random(max_delay)
        # create tasks so coroutines wait_random can all run concurrently
        delay_list = await asyncio.gather(*tasks)
        delay_list.sorted()
    return delay_list
