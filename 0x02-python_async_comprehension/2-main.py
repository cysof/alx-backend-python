#!/usr/bin/env python3

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    """
    An asynchronous function that calls the `measure_runtime` coroutine and returns its result.
    
    Returns:
        The result of the `measure_runtime` coroutine.
    """
    return await(measure_runtime())

print(
    asyncio.run(main())
)