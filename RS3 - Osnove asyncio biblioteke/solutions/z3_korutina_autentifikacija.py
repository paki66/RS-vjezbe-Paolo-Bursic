"""
Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na poslužiteljskoj strani.
Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se od ključeva korisnicko_ime, email i lozinka.
Unutar korutine simulirajte provjeru korisničkog imena na način da ćete provjeriti nalaze li se par korisnicko_ime i
    email u bazi korisnika. Ova provjera traje 3 sekunde.

Ako se korisnik ne nalazi u bazi, vratite poruku "Korisnik {korisnik} nije pronađen."

Ako se korisnik nalazi u bazi, potrebno je pozvati vanjsku korutinu autorizacija() koja
    će simulirati autorizaciju korisnika u trajanju od 2 sekunde.
Funkcija kao ulazni parametar prima rječnik korisnika iz baze i lozinku proslijeđenu iz korutine autentifikacija().
Autorizacija simulira dekripciju lozinke (samo provjerite podudaranje stringova) i provjeru s lozinkom iz baze_lozinka.
Ako su lozinke jednake, korutine vraća poruku "Korisnik {korisnik}: Autorizacija uspješna.",
    a u suprotnom "Korisnik {korisnik}: Autorizacija neuspješna.".

Korutinu autentifikacija() pozovite u main() funkciji s proizvoljnim korisnikom i lozinkom.
"""

baza_korisnika = [
  {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
  {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
  {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
  {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
  {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
  {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
  {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
  {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

autorizirani_korisnik = {
    "korisnicko_ime": "mirko123",
    "email": "mirko123@gmail.com",
    "lozinka": "lozinka123"
}

krivi_unos_lozinke = {
    "korisnicko_ime": "maja_0x",
    "email": "majaaaaa@gmail.com",
    "lozinka": "lozinka123"
}

nepostojeci_korisnik = {
    "korisnicko_ime": "ana_anic",
    "email": "majaaaaa@gmail.com",
    "lozinka": "lozinka123"
}

import asyncio

async def authenticate(korisnik):
    kljucevi_provjere = {"korisnicko_ime", "email"}
    podaci_provjere = {pod : korisnik[pod] for pod in kljucevi_provjere}
    await asyncio.sleep(3)
    if podaci_provjere not in baza_korisnika:
        return None

    return korisnik["lozinka"]


async def authorize(lozinka):  # TODO stavi zakasnjenje 2 sec
    return True


async def main(korisnik):
    korisnicko_ime = korisnik['korisnicko_ime']
    lozinka = await authenticate(korisnik)

    if not lozinka:
        return print(f"Korisnik {korisnicko_ime} nije pronađen.")

    authorized = await authorize(lozinka)

    if not authorized:
        return print(f"Korisnik {korisnicko_ime}: Autorizacija neuspješna.")

    return print(f"Korisnik {korisnicko_ime}: Autorizacija uspješna.")


asyncio.run(main(autorizirani_korisnik))  # Korisnik mirko123: Autorizacija uspješna.
asyncio.run(main(krivi_unos_lozinke))  # Korisnik maja_0x: Autorizacija neuspješna.
asyncio.run(main(nepostojeci_korisnik))  # Korisnik ana_anic nije pronađen.
