#!/usr/bin/env python3
"""
Module: Asynchronous generator module.

Provides an async coroutine looping 10 times, waiting 1 second at each
iteration, and yielding a random number between 0 and 10.
"""
import random
import asyncio


async def async_generator():
    """
    Asynchronous generator yielding random numbers.

    Loops 10 times, waits 1 second each time, and yields a random float
    between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
