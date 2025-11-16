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

"""
Objašnjenje:
(linija 25) run funkcija iz asyncio biblioteke pokreće event loop
(linija 18-20) odvija se prva faza event loop-a (Task scheduling), na event loop memoriji zakazana su 3 taska timer()
(linija 23) korutina asyncio.gather() pokreće sva 3 zakazana taska, event loop predaje kontrolu [Timer 1]
[Timer 1] izvršava kod do awaita i predaje kontrolu [Timer 2]
[Timer 2] izvršava kod do awaita i predaje kontrolu [Timer 3]
[Timer 3] izvršava kod do awaita i event loop čeka 1 sec jer su sve korutine suspendane
Ovaj proces se ponavlja 3 puta, a onda [Timer 1] izlazi iz for petlje, printa i završava svoje tijelo
[Timer 2] izvršava kod do awaita i predaje kontrolu [Timer 3]
[Timer 3] izvršava kod do awaita i event loop čeka 1 sec jer su sve korutine suspendane
Ovaj proces se ponavlja 2 puta, a onda [Timer 2] izlazi iz for petlje, printa i završava svoje tijelo
[Timer 3] prolazi još kroz 2 iteracije s razmakom od 1 sec između svake, 
    a onda izlazi iz for petlje, printa i završava svoje tijelo
 
------------------------------------------------------------------------------------------------------------------------

Output: 
Timer 1: 3 sekundi preostalo...
Timer 2: 5 sekundi preostalo...
Timer 3: 7 sekundi preostalo...
Timer 1: 2 sekundi preostalo...
Timer 2: 4 sekundi preostalo...
Timer 3: 6 sekundi preostalo...
Timer 1: 1 sekundi preostalo...
Timer 2: 3 sekundi preostalo...
Timer 3: 5 sekundi preostalo...
Timer 1: Vrijeme je isteklo!
Timer 2: 2 sekundi preostalo...
Timer 3: 4 sekundi preostalo...
Timer 2: 1 sekundi preostalo...
Timer 3: 3 sekundi preostalo...
Timer 2: Vrijeme je isteklo!
Timer 3: 2 sekundi preostalo...
Timer 3: 1 sekundi preostalo...
Timer 3: Vrijeme je isteklo!
"""
