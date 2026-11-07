import json

from fastapi import APIRouter
router = APIRouter()

with open("resources/Film.json") as filmovi_file:
    filmovi = json.load(filmovi_file)

@router.get("/filmovi")
def get_filmove():
    return filmovi


@router.get("/filmovi/{imdbID}")
def get_film_by_ID(imdbID):
    for film in filmovi:
        if film["imdbID"] == imdbID:
            return film
    return None


@router.get("/filmovi/title/{title}")
def get_film_by_title(title):
    for film in filmovi:
        if film["Title"] == title:
            return film
    return None