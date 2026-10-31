import asyncio
from turtledemo.penrose import start

import aiohttp
from aiohttp import web
import time

async def request(port, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:{port}{url}") as resp:
            return web.json_response(await resp.json())

async def main():
    start = time.perf_counter()
    task_1 = asyncio.create_task(request(8081, '/pozdrav'))
    task_2 = asyncio.create_task(request(8082, '/pozdrav'))
    result = await asyncio.gather(task_1, task_2)
    print(result)
    end = time.perf_counter()
    print(end-start)


asyncio.run(main())