#!/usr/bin/env python3
"""
Module: A file that runs functions under Python3.
asyncio: A module that runs functions under Python3.
time: A module that runs functions under Python3.
async_comprehension: A module that runs functions under Python3.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """A coroutine that will execute async_comprehension four times in
    parallel using asyncio.gather."""
    start_time = time.time()
    await asyncio.gather(async_comprehension())
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
