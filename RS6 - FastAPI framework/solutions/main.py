from fastapi import FastAPI, Response

from models import Film

filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

app = FastAPI()


@app.get("/filmovi")
def get_movies():
    checked_movies = []
    for film_dict in filmovi:
        try:
            film  = Film(**film_dict)
            checked_movies.append(film)
        except:
            continue
    return checked_movies



@app.get("/filmovi/{id}")
def get_movie(id: int):
    try:
        checked_movie = Film(**filmovi[id-1])
    except IndexError as e:
        return {'error': 'No movie with such id found'}
    return checked_movie