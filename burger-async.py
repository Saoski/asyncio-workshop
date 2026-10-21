import asyncio
import time


async def cook_burger():
    await asyncio.sleep(1)
    print("(1) Burger cooked!")


async def melt_cheese():
    await asyncio.sleep(1)
    print("(2) Cheese melted!")


async def make_cheeseburger():
    await cook_burger()
    await melt_cheese()


async def main():
    for _ in range(3):
        await make_cheeseburger()
    print("Burgers Done!")


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
