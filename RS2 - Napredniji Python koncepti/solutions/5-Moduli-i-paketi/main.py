"""
U main.py datoteci učitajte modul narudzbe.py iz paketa shop i pozovite funkciju napravi_narudzbu s listom proizvoda iz
    prethodnog zadatka.
"""

from shop import proizvodi, narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for proizvod in proizvodi_za_dodavanje:
    proizvod_objekt = proizvodi.Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["dostupna_kolicina"])
    proizvodi.dodaj_proizvod(proizvod_objekt)

print(len(proizvodi.skladiste))

for proizvod in proizvodi.skladiste:
    proizvod.ispis()

narudzba = narudzbe.napravi_narudzbu(proizvodi.skladiste)

print(narudzba.cijena)
narudzba.ispis_narudzbe()
