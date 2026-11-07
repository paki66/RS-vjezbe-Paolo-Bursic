from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class Film(BaseModel):
    title: str
    year: int = Field(gt=1900)
    rated: str
    released: datetime | None = None
    runtime: str = Field(gt=0)
    genre: str
    director: str | None = None
    writer: str | None = None
    actors: list[str]
    plot: str
    language: list[str]
    country: list[str]
    awards: str | None = None
    poster: str | None = None
    imdbRating: float | None = None
    imdbVotes: int = Field(default=None, gt=0)
    imdbID: str = Field(gt=0, lt=10)
    type: Literal['movie', 'series'] | None = None
    response: bool | None = None
    images: list[str] | None = None


class Actor(BaseModel):
    name: str
    surname: str


class Writer(BaseModel):
    name: str
    surname: str
