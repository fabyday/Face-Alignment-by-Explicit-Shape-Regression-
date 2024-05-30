import asyncio 





async def test_async_sleep(i ):
    print("test : " + str(i))
    await asyncio.sleep(5)
    print("test : " + str(i))


import time 
async def test_sleep(i ):
    print("test : " + str(i))
    time.sleep(5)
    print("test : " + str(i))




asyncio.gather(*[test_async_sleep(1),test_async_sleep(2)])
time.sleep(4)
asyncio.gather(*[test_sleep(1),test_sleep(2)])

