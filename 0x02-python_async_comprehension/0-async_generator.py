#!/usr/bin/env python3
"""Module to create async generator"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """coroutine loops 10 times, async wait 1 sec then yield
    random number each time"""
    """yields random int every 1 second delay, 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
