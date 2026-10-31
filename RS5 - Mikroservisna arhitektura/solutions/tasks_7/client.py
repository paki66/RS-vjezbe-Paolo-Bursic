import asyncio

from aiohttp import ClientSession


async def client():
    async with ClientSession() as session:
        task1 = session.post("http://localhost:8083/zbroj", json=[1,2,3,4,5,6,7,8,9,10])
        task2 = session.post("http://localhost:8084/umnozak", json=[1,2,3,4,5,6,7,8,9,10])
        output = await asyncio.gather(task1, task2)
        sum, umnozak = output
        sum = await sum.json()
        umnozak = await umnozak.json()
        microservice_3 = await session.post("http://localhost:8085/kolicnik", json={"sum": sum, "umnozak": umnozak})
        result = await microservice_3.json()
        print(result)

asyncio.run(client())