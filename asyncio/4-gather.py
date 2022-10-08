import asyncio
# future object
# https://docs.python.org/3/library/asyncio-future.html#asyncio.Future
#
# A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation.
# When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place.
# Future objects in asyncio are needed to allow callback-based code to be used with async/await.
#

async def function_that_returns_a_future_object():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    print("reading file...")
    with open('/Users/gcadet/OneDrive/Divers/IOT/ELEGOO/My Projects/python-samples/asyncio/data/library_index.json', 'rb') as f:
        return f.read(100)

async def main():
    await asyncio.gather(function_that_returns_a_future_object(), blocking_io())

if __name__ == "__main__":
    asyncio.run(main())         # get the loop - run the task - close the loop
