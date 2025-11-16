"""
Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka.
Kako se u praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od 3 sekunde.
Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva prezime, broj_kartice i CVV.
Definirajte listu s 3 rječnika osjetljivih podataka.
Pohranite u listu zadaci kao u prethodnom zadatku te pozovite zadatke koristeći asyncio.gather().
Korutina secure_data mora za svaki rječnik vratiti novi rječnik u obliku:
    {'prezime':prezime, 'broj_kartice': 'enkriptirano', 'CVV': 'enkriptirano'}.
Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash vrijednost ulaznog stringa.
"""

unsecure_data_list = [
    {"surname": "Buršić", "card_number": "A ča ćeš?", "CVV": "123"},
    {"surname": "Terlević", "card_number": "Rješiti bug!", "CVV": "345"},
    {"surname": "Pliško", "card_number": "A ča drugo!XD", "CVV": "567"},
]

import asyncio

async def secure_data(unsecure_data):
    print(f"Securing data for {unsecure_data['surname']}...")
    await asyncio.sleep(3)

    secured_data = {
        "surname": unsecure_data["surname"],
        "card_number": hash(unsecure_data["card_number"]),
        "CVV": hash(unsecure_data["CVV"])
    }

    return print(secured_data)


async def main():
    tasks = list(map(lambda data : asyncio.create_task(secure_data(data)), unsecure_data_list))
    await asyncio.gather(*tasks)


asyncio.run(main())
