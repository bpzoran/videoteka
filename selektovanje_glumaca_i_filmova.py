from film import Film
from glumac import Glumac
from kreiranje_konekcije import get_connection

def izlistaj_glumce_i_filmove():
    glumci = {}
    filmovi = {}
    with get_connection() as cnx:
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT g.id as id_glumca, g.ime_glumca, g.datum_rodjenja, "
                                    "g.drzava_porekla, f.id as id_filma, f.naziv_filma, "
                                    "f.trajanje_u_minutima, f.zanr_filma, f.godina_produkcije, "
                                    "f.ocena FROM glumac g inner join film_glumac fg on g.id=fg.id_glumca "
                                    "inner join film f on fg.id_filma=f.id")
            rows = cursor.fetchall()
            for row in rows:
                if not glumci.get(row["id_glumca"]):
                    glumac = Glumac(id_glumca=row["id_glumca"],
                                    ime_glumca=row["ime_glumca"],
                                    datum_rodjenja=row["datum_rodjenja"],
                                    drzava_porekla=row["drzava_porekla"],
                                    )
                    glumci[row["id_glumca"]] = glumac
                if not filmovi.get(row["id_filma"]):
                    film = Film(id_filma=row["id_filma"], naziv_filma=row["naziv_filma"],
                                trajanje_u_minutima=row["trajanje_u_minutima"],
                                zanr_filma=row["zanr_filma"],
                                godina_produkcije=row["godina_produkcije"],
                                ocena=row["ocena"]
                                )
                    filmovi[row["id_filma"]] = film
                glumci[row["id_glumca"]].filmovi.append(filmovi[row["id_filma"]].naziv_filma)
                filmovi[row["id_filma"]].glumci.append(glumci[row["id_glumca"]].ime_glumca)


    return glumci, filmovi
