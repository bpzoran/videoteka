from datetime import date
from typing import List
from pydantic import BaseModel

class Glumac(BaseModel):
    id_glumca: int
    ime_glumca: str
    datum_rodjenja: date
    drzava_porekla: str
    filmovi: List[str] = []

    def __str__(self):
        return f"{self.ime_glumca}; {self.datum_rodjenja}; {self.drzava_porekla}; Filmovi: {self.filmovi_str()}"

    def filmovi_str(self):
        return ", ".join([f for f in self.filmovi])
