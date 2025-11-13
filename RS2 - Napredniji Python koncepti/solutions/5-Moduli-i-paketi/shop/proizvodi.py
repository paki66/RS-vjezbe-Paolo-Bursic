"""
definirajte klasu Proizvod s atributima naziv, cijena i dostupna_kolicina.
Dodajte metodu ispis koja će ispisivati sve atribute proizvoda.

u listu skladiste pohranite 2 objekta klase Proizvod s proizvoljnim vrijednostima atributa.
U ovoj listi ćete pohranjivati instance klase Proizvod koje će predstavljati stanje proizvoda u skladištu.

definirajte funkciju dodaj_proizvod van definicije klase koja će dodavati novi Proizvod u listu skladiste.

U main.py datoteci učitajte modul proizvodi.py iz paketa shop i pozovite pozovite funkciju dodaj_proizvod za
    svaki element iz sljedeće liste: <proizvodi_za_dodavanje> u kodu

Lista skladiste treba sada sadržavati ukupno 6 elemenata.

Nakon što to napravite, pozovite metodu ispis za svaki proizvod iz liste skladiste.
"""



class Proizvod():
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        return print(f"Proizvod: naziv={self.naziv}, cijena={self.cijena}, dostupna_kolicina={self.dostupna_kolicina}")


mobitel = Proizvod("Mobitel", 400, 70)
slusalice = Proizvod("Slusalice", 150, 5)

skladiste = [mobitel, slusalice]

def dodaj_proizvod(proizvod: Proizvod):
    skladiste.append(proizvod)

