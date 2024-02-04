from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from film import Film
from glumac import Glumac
from selektovanje_glumaca_i_filmova import izlistaj_glumce_i_filmove

from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/filmovi/", response_model=List[Film])
def izlistaj_filmove():
    return list(izlistaj_glumce_i_filmove()[1].values())

@app.get("/glumci/", response_model=List[Glumac])
def izlistaj_glumce():
    return list(izlistaj_glumce_i_filmove()[0].values())
