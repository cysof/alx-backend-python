#!/usr/bin/env python3
import asyncio
import random
from typing import Generator

""" Module that contain a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second, 
then yield a random number between 0 and 10. Use the random module.

"""

async def async_generator():
    """
    An asynchronous generator that yields random float numbers between 0 and 10.

    This function uses the `asyncio.sleep` coroutine to asynchronously wait for 1 second
    before yielding a random float number between 0 and 10. The function loops 10 times
    and returns a generator that can be iterated over asynchronously.

    Returns:
        Generator[float]: A generator that yields random float numbers between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
