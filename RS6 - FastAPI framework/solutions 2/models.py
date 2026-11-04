from typing import Literal

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
