"""
Definirajte klasu Automobil s atributima marka, model, godina_proizvodnje i kilometraža.
Dodajte metodu ispis koja će ispisivati sve atribute automobila.

Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis.

Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama,
    trenutnu godine dohvatite pomoću datetime modula.
"""

import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        return print(f"Marka: {self.marka}, Model: {self.model}, Godina proizvodnje: {self.godina_proizvodnje}, " +
                     f"Kilometraza: {self.kilometraza}")

    def starost(self):
        danas = datetime.date.today().year
        godina = int(self.godina_proizvodnje)

        razlika = danas - godina

        return print(f"Automobil je star {razlika} godina")


crveni_vrag = Automobil("Alfa Romeo", "156", "1999", "650,000")

crveni_vrag.ispis()
crveni_vrag.starost()
