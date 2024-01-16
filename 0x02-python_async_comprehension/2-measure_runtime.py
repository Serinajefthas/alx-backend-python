#!/usr/bin/env python3
"""Module to create async coroutine"""
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures total runtime of async comp when run 4x in parallel"""
    start_time = asyncio.get_event_loop().time()
    """cant use for loop as just wait for executing next coroutine, but
    want call it asynchronously in this case"""
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = asyncio.get_event_loop().time()
    runtime = end_time - start_time
    return runtime
