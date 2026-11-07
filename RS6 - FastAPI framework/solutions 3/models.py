from pydantic import BaseModel


class BaseAutomobil(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    boja: str


class AutomobilRequest(BaseAutomobil):
    cijena: float


class AutomobilResponse(BaseAutomobil):
    id: int
    cijena_pdv: float