#!/usr/bin/env python3
"""
Module: A file that runs functions under Python3.
asyncio: A module that runs functions under Python3.
async_comprehension: A module that runs functions under Python3.
"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """A coroutine that will execute async_comprehension four times in
    parallel using asyncio.gather."""
    return await asyncio.gather(async_comprehension())
