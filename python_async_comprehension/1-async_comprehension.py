#!/usr/bin/env python3
"""
Module: A file that runs functions under Python3.
asyncio: A module that runs functions under Python3.
random: A module that runs functions under Python3.
async_generator: A module that runs functions under Python3.
"""
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """The coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers."""
    return [i async for i in async_generator()]
