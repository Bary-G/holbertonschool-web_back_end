#!/usr/bin/env python3
"""
Module: All used Python3 modules.
time: The time module for Python3.
asyncio: All used Python3 modules.
wait_n: An async routine called wait_n that takes in 2 int arguments: n and
max_delay. wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """A measure_time function with integers n and max_delay as arguments that
    measures the total execution time for wait_n(n, max_delay), and returns
    total_time / n."""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
