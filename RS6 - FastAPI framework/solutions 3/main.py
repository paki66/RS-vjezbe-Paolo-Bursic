from fastapi import FastAPI, HTTPException
from fastapi import Query

from models import AutomobilRequest, AutomobilResponse, BaseAutomobil

automobili: list[AutomobilResponse] = [
    AutomobilResponse(id= 1, marka= "Merceedes", model= "C-klasa",  cijena_pdv= 3000.00, godina_proizvodnje= 2004, boja= "crna")
]

app = FastAPI()

@app.get("/automobili/{id}", response_model=AutomobilResponse)
def get_automobile(id: int, max_cijena: float | None = 10000000, max_godina: int | None = 2026, min_cijena: float = Query(default=200, gt=0), min_godina: int = Query(default= 2000, ge=1960)):
    if min_godina > max_godina or min_cijena > max_cijena:
        raise HTTPException(detail={'error': "Please enter correct query params"}, status_code=422)
    for automobile in automobili:
        if automobile.id == id:
            return automobile
    raise HTTPException(detail={'error': "No automobile with this id"}, status_code=404)

@app.post("/automobili", response_model=AutomobilResponse)
def create_automobile(automobil: AutomobilRequest):
    for existing in automobili:
        if existing.model_dump(exclude={"id", "cijena_pdv"}) == automobil.model_dump(exclude={"cijena"}):
            raise HTTPException(detail={'error': "Car is already created"}, status_code=409)

    id = len(automobili) + 1
    cijena_pdv = automobil.cijena * 1.25
    automobil_response = AutomobilResponse(id=id, cijena_pdv=cijena_pdv, **automobil.model_dump())


    automobili.append(automobil_response)
    return automobil_response