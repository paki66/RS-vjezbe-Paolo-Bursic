from pydantic import BaseModel


class Automobil(BaseModel):
    id: str
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str