import asyncio
import aiohttp

async def main():
    async with (aiohttp.ClientSession() as session):
        amount = 8
        task_1 = asyncio.create_task(session.get(f"http://localhost:8086/cat/{amount}"))
        data_1 = await task_1
        facts = await data_1.json()
        print(facts)
        task_2 = asyncio.create_task(session.patch("http://localhost:8087/facts", json=facts))
        data_2 = await task_2
        filtered_facts = await data_2.json()
        print(filtered_facts)


asyncio.run(main())