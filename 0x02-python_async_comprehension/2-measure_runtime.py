#!/urs/bin/env python3
from random import uniform
import asyncio
from typing import Generator, List
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Asynchronously measures the runtime of the `async_comprehension` function by executing it 4 times concurrently.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time()
    async_ = [async_comprehension() for numb in range(4)]
    result = await asyncio.gather(*async_)
    end_time = time()

    """
    This code snippet defines an asynchronous function 
    called measure_runtime that measures the runtime of 
    the async_comprehension function. It does this by executing 
    async_comprehension four times concurrently 
    using the asyncio.gather function. The function starts a 
    timer before executing the async_comprehension function,
    then waits for all the concurrent executions to complete 
    using await asyncio.gather(*async_). Finally, it stops the timer 
    using the time function and calculates the total runtime in seconds. 
    The function returns the total runtime as a float."""

    return end_time - start_time 


