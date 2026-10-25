"""
Napišite korutinu autentifikacija koja simulira proces autentifikacije korisnika. Korutina treba primiti korisničko ime i
lozinku, zatim simulirati sporo I/O čekanje (npr. 2 sekunde) prije nego što vrati True ako su korisničko ime i lozinka ispravni.
Korisničko ime i lozinku provjerite prema rječniku korisnici koji sadrži parove korisničko ime-lozinka.

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}
Simulirajte pogrešku u autentifikaciji ako su uneseni podaci netočni (raise ValueError).

Napišite glavnu funkciju koja će poslati konkurentne zahtjeve za autentifikaciju za 5 različitih korisnika (neki s ispravnim,
neki s neispravnim podacima). Kako se ponaša asyncio.gather() kada se dogodi iznimka u jednoj od korutina?

Izmijenite kod korutine i simulirajte grešku u autentifikaciji koja se javlja odmah nakon 3 sekunde čekanja
(npr. ne radi autentifikacijski servis) koji će podići iznimku TimeoutError.

Dodajte timeout prilikom poziva korutine autentifikacija kako biste simulirali situaciju kada autentifikacijski servis ne odgovara na vrijeme.
"""
import asyncio

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}

async def auth(username, password):
    await asyncio.sleep(4)
    if username in korisnici.keys() and korisnici[username] == password:
        return True
    else:
        raise ValueError


async def main():
    await asyncio.wait_for(auth("korisnik1", "lozinka1"), timeout=3)  # Timeout Error

    task1 = asyncio.create_task(auth("korisnik1", "lozinka1"))
    task2 = asyncio.create_task(auth("admin", "dfg"))
    task3 = asyncio.create_task(auth("korisnik2", "lozinka3"))
    task4 = asyncio.create_task(auth("korisnik2", "lozinka2"))
    task5 = asyncio.create_task(auth("korisnik3", "lozinka3"))

    await asyncio.gather(task1, task2, task3, task4, task5)  # ValueError

asyncio.run(main())