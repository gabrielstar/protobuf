import asyncio


# sequential code will run in order at a speed of our processor (1 thread - 1 procesor)
# async allows to run code while other is not finished yet

def foo():
    return


foo()
print('Gab Sync')


# coroutines - wrapped version of function that allows it to run asynchronously
async def main():  # it created a wrapper, when it is called it will return a coroutine
    print('Gab Coroutine')
    #await text("hey")
    task = asyncio.create_task(text("hey")) #task allows us to run sth else in the meantime
    await asyncio.sleep(0.5)
    print("Done")


async def text(text):
    print(text)
    await asyncio.sleep(2)


# print(main()) #coroutine
# await main() #await must be within async - we need to define an event-loop - lower level thing
asyncio.run(main())  # asyncio create an eventloop
