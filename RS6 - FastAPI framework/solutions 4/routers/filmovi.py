import json
import re
from typing import Literal

from fastapi import APIRouter, HTTPException

router = APIRouter()

with open("resources/Film.json") as filmovi_file:
    filmovi = json.load(filmovi_file)

@router.get("/filmovi")
def get_filmove(min_year: int = 1960, max_year: int = 2026, min_rating: float = 0, max_rating: float = 10, type: Literal["movie", "series"] = None):
    response = []
    for film in filmovi:
        film_year = ''.join([char for char in film['Year'] if char.isdigit()])
        if max_year > int(film_year) > min_year:
            response.append(film)
    for film in filmovi:
        if film["imdbRating"] is not 'N/A':
            response.append(film)
            continue
        if max_rating > float(film['imdbRating']) > min_rating:
            response.append(film)
    if type:
        response = [film for film in response if film["Type"] == type]
    return response


@router.get("/filmovi/{imdbID}")
def get_film_by_ID(imdbID):
    for film in filmovi:
        if film["imdbID"] == imdbID:
            return film
    raise HTTPException(status_code=404, detail="Film not found")


@router.get("/filmovi/title/{title}")
def get_film_by_title(title):
    for film in filmovi:
        if film["Title"] == title:
            return film
    raise HTTPException(status_code=404, detail="Film not found")
