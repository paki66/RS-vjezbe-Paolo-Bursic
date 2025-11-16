"""
Definirajte korutinu provjeri_parnostkoja će simulirati "super zahtjevnu operaciju" provjere parnosti broja putem vanjskog API-ja.
Korutina prima kao argument broj za koji treba provjeriti parnost, a vraća poruku "Broj {broj} je paran." ili
    "Broj {broj} je neparan." nakon 2 sekunde.
Unutar main funkcije definirajte listu 10 nasumičnih brojeva u rasponu od 1 do 100 (koristite random modul).
Listu brojeva izgradite kroz list comprehension sintaksu.
Nakon toga, pohranite u listu zadaci 10 Task objekata koji će izvršavati korutinu provjeri_parnost za
    svaki broj iz liste (također kroz list comprehension).
Na kraju, koristeći asyncio.gather(), pokrenite sve korutine konkurentno i ispišite rezultate.
"""