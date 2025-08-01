#!/usr/bin/env python3
"""
Module: A file that runs functions under Python3.
asyncio: A module that runs functions under Python3.
random: A module that runs functions under Python3.
typing: A module that runs functions under Python3.
"""
import asyncio
import random
import typing


async def wait_random(max_delay: int = 10) -> float:
    """An asynchronous coroutine that takes in an integer argument (max_delay,
    with a default value of 10) named wait_random that waits for a random
    delay between 0 and max_delay (included and float value) seconds and
    eventually returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """An async routine called wait_n that takes in 2 int arguments: n and
    max_delay. wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency."""
    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
