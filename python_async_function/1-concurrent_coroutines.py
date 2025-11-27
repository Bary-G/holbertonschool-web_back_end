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
    return selection_sort(results)

def selection_sort(lst):
    """Sorts a list by ascendant order using selection sort"""
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
