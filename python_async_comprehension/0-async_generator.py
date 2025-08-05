#!/usr/bin/env python3
"""
Module: A file that runs functions under Python3.
asyncio: A module that runs functions under Python3.
random: A module that runs functions under Python3.
"""
import asyncio
import random


async def async_generator():
    """A coroutine that loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
