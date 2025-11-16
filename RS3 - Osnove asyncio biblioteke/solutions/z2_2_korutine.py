"""
Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba.
Prva korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde,
a druga korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5 sekundi.
Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate.
Program se mora izvršavati ~5 sekundi.
"""

import asyncio, time

async def get_users():
    users = [
        {"name": "Jože", "status": "Active", "money spent": 110},
        {"name": "Marko", "status": "Disabled", "money spent": 20},
        {"name": "Ivan", "status": "Waiting", "money spent": 0}
    ]

    await asyncio.sleep(3)

    return users


async def get_products():
    products = [
        {"name": "bread", "price": 20},
        {"name": "eggs", "price": 15},
        {"name": "milk", "price": 10},
        {"name": "plastic bag", "price": "Too much"}
    ]

    await asyncio.sleep(5)

    return products


async def main():
    return await asyncio.gather(get_users(), get_products())



t1 = time.perf_counter()
results = asyncio.run(main())
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
