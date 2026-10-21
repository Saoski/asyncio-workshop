import time


def cook_burger():
    time.sleep(1)
    print("(1) Burger cooked!")

def melt_cheese():
    time.sleep(1)
    print("(2) Cheese melted!")

def make_cheeseburger():
    cook_burger()
    melt_cheese()


def main():
    for _ in range(3):
        make_cheeseburger()
    print("Burgers Done!")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
