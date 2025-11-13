"""
definirajte klasu Narudzba s atributima: naruceni_proizvodi i ukupna_cijena.

dodajte funkciju napravi_narudzbu van definicije klase koja prima listu proizvoda kao argument i
    vraća novu instancu klase Narudzba.

dodajte provjeru u funkciju napravi_narudzbu koja će provjeravati dostupnost proizvoda prije nego što se napravi narudžba.
    Ako proizvoda nema na stanju, ispišite poruku: "Proizvod {naziv} nije dostupan!" i ne stvarajte narudžbu.

dodajte provjere u funkciju napravi_narudzbu koja će provjeriti sljedeća 4 uvjeta:

argument naruceni_proizvodi mora biti lista

svaki element u listi mora biti rječnik

svaki rječnik mora sadržavati ključeve naziv, cijena i narucena_kolicina

lista ne smije biti prazna

izračunajte ukupnu cijenu narudžbe koju ćete pohraniti u lokalnu varijablu ukupna_cijena u jednoj liniji koda.

narudžbe (instanca klase Narudzba) pohranite u listu rječnika narudzbe.

u klasu Narudzba dodajte metodu ispis_narudzbe koja će ispisivati nazive svih naručenih proizvoda,
    količine te ukupnu cijenu narudžbe.

npr. "Naručeni proizvodi: Laptop x 2, Monitor x 1, Ukupna cijena: 11000 eur".
"""

from functools import reduce
from . import proizvodi

class Narudzba:
    def __init__(self, naruceni_proizvodi, cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.cijena = cijena

    def ispis_narudzbe(self):
        stavke_narudzbe = [f"{stavka.naziv} × {self.naruceni_proizvodi.count(stavka)}" for stavka in set(self.naruceni_proizvodi)]
        return print(f"Naruceni proizvodi: {stavke_narudzbe}, Ukupna cijena: {self.cijena} eur")

narudzbe = []

def napravi_narudzbu(naruceni_proizvodi: list[proizvodi.Proizvod]):
    is_proizvodi_lista = isinstance(naruceni_proizvodi, list)
    svi_proizvodi_rjecnik = all([isinstance(p, proizvodi.Proizvod) for p in naruceni_proizvodi])
    proizvodi_neprazni = len(naruceni_proizvodi) >= 1

    uvjeti_ispunjeni = is_proizvodi_lista and svi_proizvodi_rjecnik and proizvodi_neprazni
    if not uvjeti_ispunjeni:
        return print(f"Narudzba ne moze biti kreirana")

    for p in naruceni_proizvodi:
        if p.dostupna_kolicina < 1:
            return print(f"Proizvod {p.naziv} nije dostupan")

    cijene_proizvoda = list(map(lambda p : p.cijena, naruceni_proizvodi))
    ukupni_iznos = reduce(lambda agg, x : agg + x, cijene_proizvoda)

    nova_narudzba = Narudzba(naruceni_proizvodi, ukupni_iznos)
    narudzbe.append(nova_narudzba)

    return nova_narudzba


