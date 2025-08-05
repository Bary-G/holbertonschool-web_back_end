#!/usr/bin/env python3
"""
Module: This module provides an asynchronous coroutine called wait_random and
a function task_wait_random that wraps the coroutine in an asyncio Task.

asyncio: Import asyncio to work with asynchronous operations

wait_random: An asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits for a
random delay between 0 and max_delay (included and float value) seconds and
eventually returns it.
"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function task_wait_random that takes an integer max"""
    return asyncio.create_task(wait_random(max_delay))
