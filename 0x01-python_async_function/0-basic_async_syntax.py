#!/usr/bin/env python3
"""Module for an asynchronous coroutine function"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Function waits for random delay then returns"""
    random_delay = random.uniform(0.0, max_delay)
    await asyncio.sleep(random_delay)
