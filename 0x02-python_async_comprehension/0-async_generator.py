#!/usr/bin/env python3
"""Module to create async generator"""
import asyncio
from typing import Generator
import random


async def async_generator() -> int:
    """coroutine loops 10 times, async wait 1 sec then yield
    random number each time"""
    """yields random int every 1 second delay, 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        randnum = random.randint(0, 10)
        yield randnum
    return randnum

asyncio.run(async_generator)