#!/usr/bin/env python3

""" Module that contains an asynchronous coroutine that takes an integer
argument (max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay (included float value)
seconds and eventually returns it.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and the given maximum delay.

    Args:
        max_delay (int, optional): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay in seconds.
    """
    """
    Asynchronously waits for a random delay between 0 and the given maximum delay.

    Args:
        max_delay (int, optional): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay