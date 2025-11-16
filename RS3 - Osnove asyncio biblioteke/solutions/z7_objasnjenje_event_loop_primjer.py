"""
Objasnite korak po korak kako se ponaša event loop (kako se raspoređuju, izvršavaju i
    dovršavaju korutine te koja su njihova stanja u različitim fazama izvođenja) u sljedećem primjeru:

(P.B.) Kod je copy-paste iz task definition-a, ja san doda komentare.
"""

import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    await asyncio.gather(*timers)

asyncio.run(main())
