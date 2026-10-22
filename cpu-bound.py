import asyncio
import time

ANSWERS_TO_THE_UNIVERSE = 3


async def async_compute_the_answer_to_the_universe():
    print("Started computing!")
    answer = 1
    for _ in range(200_000):
        answer *= 2
    answer = 42
    return 42


def compute_the_answer_to_the_universe():
    print("Started computing!")
    answer = 1
    for _ in range(200_000):
        answer *= 2
    answer = 42
    return 42


async def async_main():
    async with asyncio.TaskGroup() as tg:
        [
            tg.create_task(async_compute_the_answer_to_the_universe())
            for _ in range(3)
        ]


def main():
    for _ in range(3):
        compute_the_answer_to_the_universe()


# async def threading_main():
#     threads = [asyncio.to_thread(compute_the_answer_to_the_universe) for _ in range(3)]
#     for thread in threads:
#         await thread


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(async_main())
    elapsed = time.perf_counter() - start
    print(f"async executed in {elapsed:0.2f} seconds.")

    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"sync executed in {elapsed:0.2f} seconds.")

    # start = time.perf_counter()
    # asyncio.run(threading_main())
    # elapsed = time.perf_counter() - start
    # print(f"threads executed in {elapsed:0.2f} seconds.")
