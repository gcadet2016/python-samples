import asyncio

# coroutine
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()

    # Equivalent to asyncio.run(main())
    loop=asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


