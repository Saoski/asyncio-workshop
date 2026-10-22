import asyncio
import time

import httpx
import requests

DUMMY_URL = "https://dummyjson.com"
REQUEST_COUNT = 20


async def make_request():
    print("Start")
    requests.get(DUMMY_URL)
    print("End")


async def make_request_thread():
    await asyncio.to_thread(requests.get, url=DUMMY_URL)


async def make_requests():
    async with asyncio.TaskGroup() as tg:
        for _ in range(REQUEST_COUNT):
            tg.create_task(make_request())


async def make_requests_threads():
    async with asyncio.TaskGroup() as tg:
        for _ in range(REQUEST_COUNT):
            tg.create_task(make_request_thread())


async def make_requests_httpx():
    async with httpx.AsyncClient() as client, asyncio.TaskGroup() as tg:
        for _ in range(REQUEST_COUNT):
            tg.create_task(client.get(DUMMY_URL))


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(make_requests())
    elapsed = time.perf_counter() - start
    print(f"executed in {elapsed:0.2f} seconds.")
    start = time.perf_counter()
    asyncio.run(make_requests_threads())
    elapsed = time.perf_counter() - start
    print(f"executed in {elapsed:0.2f} seconds.")
    start = time.perf_counter()
    asyncio.run(make_requests_httpx())
    elapsed = time.perf_counter() - start
    print(f"executed in {elapsed:0.2f} seconds.")
