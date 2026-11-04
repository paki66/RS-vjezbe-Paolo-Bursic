from fastapi import FastAPI, HTTPException
from fastapi import Query

automobili = [
    {"id": 1, "marka": "Merceedes", "model": "C-klasa",  "cijena": 3000.00, "godina_proizvodnje": 2004, "boja": "crna"}
]

app = FastAPI()

@app.get("/automobil/{id}")
def get_automobile(id: int, max_cijena: float, max_godina: int, min_cijena: float = Query(gt=0), min_godina: int = Query(ge=1960)):
    if min_godina > max_godina or min_cijena > max_cijena:
        raise HTTPException(detail={'error': "Please enter correct query params"}, status_code=422)
    for automobile in automobili:
        if automobile["id"] == id:
            return automobile
    raise HTTPException(detail={'error': "No automobile with this id"}, status_code=404)