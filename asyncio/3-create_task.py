import asyncio

# coroutine
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    task1 = asyncio.create_task(count())
    task2 = asyncio.create_task(count())
    task3 = asyncio.create_task(count())
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    await task3

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())         # get the loop - run the task - close the loop
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


 