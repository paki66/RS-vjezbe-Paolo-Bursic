"""
Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u: https://jsonplaceholder.typicode.com/users.
Morate simulirate slanje 5 zahtjeva konkurentno unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, a
rezultate pohranite u listu odjedanput koristeći asyncio.gather funkciju.
Nakon toga koristeći map funkcije ili list comprehension izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i samo username korisnika.
Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.
"""

import asyncio
import aiohttp
import time


async def fetch_users():
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://jsonplaceholder.typicode.com/users")
        return await response.json()

async def main():
    start = time.perf_counter()
    tasks = [fetch_users() for _ in range(5)]
    users = await asyncio.gather(*tasks)

    names, mails, usernames = [], [], []

    for user in users[4]:
        names.append(user["name"])
        mails.append(user["email"])
        usernames.append(user["username"])

    print(names)
    print(mails)
    print(usernames)

    end = time.perf_counter()
    print(f"{end - start} seconds")

asyncio.run(main())