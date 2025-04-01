import asyncio

# asynchronous generator function
async def async_numbers():
    for i in range(2):
        yield i

# main function
async def main():
    agen = async_numbers()  # Create an async generator
    print(await anext(agen, 'End'))
    print(await anext(agen, 'End'))
    print(await anext(agen, 'End'))

asyncio.run(main()) # calling main function