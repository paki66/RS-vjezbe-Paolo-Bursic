from fastapi import FastAPI, HTTPException

automobili = []

app = FastAPI()

@app.get("/automobil/{id}")
def get_automobile(id: int):
    for automobile in automobili:
        if automobile["id"] == id:
            return automobile
    raise HTTPException(detail={'error': "No automobile with this id"}, status_code=404)