#!/usr/bin/env python3
"""
Module: Returns the list of all the delays (float values)
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """
    Returns the list of all the delays (float values)
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return results
