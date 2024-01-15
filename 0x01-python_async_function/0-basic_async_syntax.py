#!/usr/bin/env python3
"""Module for an asynchronous coroutine function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function waits for random delay then returns"""
    random_delay = random.uniform(0.0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

asyncio.run(wait_random())
