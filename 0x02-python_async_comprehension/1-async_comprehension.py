#!/usr/bin/env python3
import asyncio
import random
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Asynchronously generates a list of random float numbers using async comprehension.

    This function uses the `async_generator` coroutine to generate random float numbers.
    It then uses async comprehension to asynchronously iterate over the generator and
    collect the numbers into a list.

    Returns:
        List[float]: A list of random float numbers.
    """
    return [i async for i in async_generator()]