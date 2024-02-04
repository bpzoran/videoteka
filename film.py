from typing import List
from pydantic import BaseModel

class Film(BaseModel):
    id_filma: int
    naziv_filma: str
    trajanje_u_minutima: int
    zanr_filma: str
    godina_produkcije: int
    ocena: float
    glumci: List[str] = []

    def __str__(self):
        return f"{self.naziv_filma}; {self.trajanje_u_minutima} minuta; {self.zanr_filma}; {self.godina_produkcije}; Glumci: {self.glumci_str()}"

    def glumci_str(self):
        return ", ".join([g for g in self.glumci])
