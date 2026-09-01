import csv
import unicodedata
from pathlib import Path


def normalise_name(name):
    """Make names comparable, e.g. turn 'Zoë' into 'zoe'."""
    return "".join(
        character
        for character in unicodedata.normalize("NFD", name.strip().split()[0].lower())
        if not unicodedata.combining(character)
    )


with open(Path(__file__).parent / "Learningteams.csv", encoding="utf-8", newline="") as file:
    LEERTEAMS = {
        normalise_name(row["voornaam"]): int(row["lt"])
        for row in csv.DictReader(file)
    }


def solution_station_5(name):
    return LEERTEAMS[normalise_name(name)]




