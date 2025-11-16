"""
Kako možete unutar main korutine natjerati event loop da obuhvati ispis unutar korutine fetch_data(2) bez
    da ju awaitate unutar main funkcije.
Preciznije, dokažite kako se može ispisati tekst Dovršio sam s 2. unutar korutine fetch_data(2) bez
    da eksplicitno pozivate await task2 unutar main() funkcije.

(P.B.) Ovaj inicijalni kod cu modificirati:
import asyncio, time

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1)) # schedule
    task2 = asyncio.create_task(fetch_data(2)) #schedule
    result1 = await task1
    print("Fetch 1 uspješno završen.")
    return [result1]


t1 = time.perf_counter()
results = asyncio.run(main()) # pokretanje event loop-a
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
"""

import asyncio, time

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1)) # schedule
    task2 = asyncio.create_task(fetch_data(2)) #schedule
    await asyncio.sleep(3)
    result1 = await task1
    print("Fetch 1 uspješno završen.")
    return [result1]


t1 = time.perf_counter()
results = asyncio.run(main()) # pokretanje event loop-a
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")