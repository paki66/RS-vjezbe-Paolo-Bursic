"""
Radite na raspodijeljenom sustavu za dohvaćanje vremenskih podataka s različitih javnih API-ja**.
Vaš servis treba konkurentno agregirati podatke o vremenu iz više izvora te nakon toga izračunati i ispisati prosječnu temperaturu.
Definirajte korutinu fetch_weather_data (predstavlja mikroservis koji vraća podatke s meteorološke stanice na određenoj lokaciji),
koja simulira određeno čekanje (možete staviti nasumično čekanje između 1 i 5 sekundi koristeći random.uniform(1, 5))
i vraća nasumičnu temperaturu između 20 i 25 stupnjeva Celzijusa.
U glavnoj korutini main kreirajte i rasporedite 10 objekata tipa Task za konkurentno dohvaćanje vremenskih podataka s 10
različitih vremenskih stanica. Nakon što dobijete sve rezultate, izračunajte i ispišite prosječnu temperaturu.

Simulirajte situaciju u kojoj nekoliko vremenskih stanica ne odgovara na vrijeme te pravilno obradite iznimku TimeoutError.

Ograničite vrijeme čekanja na svaki zahtjev na najviše 2 sekunde; u suprotnom slučaju vratite None te izračunajte prosječnu temperaturu bez podataka za tu mjernu stanicu.

Ako hoćete, možete određene dijelove koda rasporediti u zasebne datoteke (module) ili možete sve napisati u jednoj datoteci.
"""
import asyncio
import random

locations = ["Zagreb", "Split", "Pula", "Rijeka", "Osijek", "Vinkovci", "Pazin", "Dubrovnik", "Zadar", "Šibenik"]

async def fetch_weather_data(location):
    try:
        await asyncio.wait_for(asyncio.sleep(random.uniform(1, 5)), timeout=2)
        return location, random.randint(20, 25)
    except asyncio.TimeoutError:
        return location, None

async def main():
    tasks = [asyncio.create_task(fetch_weather_data(location)) for location in locations]
    results = await asyncio.gather(*tasks)
    print(results)
    temperatures = list(map(lambda x: x[1], results))
    temperatures = list(filter(None, temperatures))
    ars = sum(temperatures) / len(temperatures)
    print(ars)

asyncio.run(main())