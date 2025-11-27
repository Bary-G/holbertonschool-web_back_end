#!/usr/bin/env python3
"""
Module: Returns the list of all the delays (float values)
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns the list of all the delays (float values)
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
