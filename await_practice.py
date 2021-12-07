import asyncio
# create a coroutine first
# create a function with async keyword which creates a wrapper around a function and when the function is called
# it will return a coroutined object. This coroutine object is just like a function and it can be executed. To execute a
# coroutine we have to do is await


async def main():
    task = asyncio.create_task(foo())
    print("A")
    await asyncio.sleep(1)
    print("B")
    return_value = await task
    print(f"Return value was {return_value}")
# asyncio.run(main())


async def foo():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10

asyncio.run(main())
