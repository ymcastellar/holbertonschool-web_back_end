#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """should measure the total runtime and return it."""
    t1 = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    t2 = time.perf_counter()
    return t2 - t1
