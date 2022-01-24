import asyncio


async def fetch_data():
    print('Start fetching')
    await asyncio.sleep(2)
    print('Done fetching')
    return {
        'data': 1
    }


async def print_data():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    #they start in the same time
    task1 = asyncio.create_task(fetch_data()) #task subclasses a future
    task2 = asyncio.create_task(print_data())  # returns a future which is like promise in JS

    #wait until data is there
    value = await task1
    print(value)
    #wait for second task to finish too
    await task2 #futures need to be awaited otherwise code esxecution will end before we get data

asyncio.run(main())
