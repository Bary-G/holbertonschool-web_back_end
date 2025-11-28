#!/usr/bin/env python3
"""
Module: An asynchronous coroutine that loop 10 times,
each time asynchronously wait 1 second, then yield a random number
between 0 and 10
"""
import random
import asyncio
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    An asynchronous coroutine that loop 10 times,
    each time asynchronously wait 1 second, then yield a random number
    between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
