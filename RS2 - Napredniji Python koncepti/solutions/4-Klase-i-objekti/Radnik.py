"""
Definirajte klasu Radnik s atributima ime, pozicija, placa. Dodajte metodu work
    koja će ispisivati "Radim na poziciji {pozicija}".

Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department.
    Dodajte metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".

U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i
    povećava plaću radnika (Radnik) za iznos povecanje.

Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i give_raise.
"""

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji{self.pozicija}")


class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji{self.pozicija} u odjelu {self.department}")

    def give_raise(self, radnik: Radnik, povecanje):
        iznos_povecanja = int(povecanje)
        radnik.placa += iznos_povecanja


backend_dev = Radnik("Tone", "Backend Developer", 2000)
team_man = Manager("Nino", "Team Lead", 3500, "Important Department")

backend_dev.work()
team_man.work()
team_man.give_raise(backend_dev, 500)

print(f"{backend_dev.ime} je kuntenat ({backend_dev.placa} €)!!!")
