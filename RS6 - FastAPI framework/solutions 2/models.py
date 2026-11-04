from typing import Literal, TypedDict

from pydantic import BaseModel

from datetime import datetime


class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godine_izdavanja: int = datetime.now().strftime('%Y')
    broja_stranica: int
    izdavac: Izdavac


class Izdavac(BaseModel):
    naziv: str
    adresa: str


class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: Literal['dodavanje', 'brisanje', 'azuriranje', 'citanje'] = []


class RestaurantOrder():
    id: int
    ime_kupca: str
    stol_info: Stol_info
    lista_jela: list[Jelo]
    ukupna_cijene: float

class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float


class Stol_info(TypedDict):
    broj: int
    location: str


class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: tuple[float, float] = [0.0, 0.0]