#!/usr/bin/env python3
"""
Module: A file that runs functions under Python3.
asyncio: A module that runs functions under Python3.
random: A module that runs functions under Python3.
async_comprehension: A module that runs functions under Python3.
time: A module that runs functions under Python3.
"""
import asyncio
import random
import time

async def async_generator():
    """A coroutine that loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def async_comprehension():
    """The coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers."""
    return [i async for i in async_generator()]

async def measure_runtime():
    start_time = time.time()
    await asyncio.gather(async_comprehension())
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime