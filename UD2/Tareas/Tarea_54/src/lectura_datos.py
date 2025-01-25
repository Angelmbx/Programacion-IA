import pandas as pd
from seres_biologicos import Seres_biologicos
from droides import Droides

url = "UD2/Tareas/Tarea_54/starwars.csv"

archivo = pd.read_csv(url)

filas = archivo.to_dict(orient='records')

personajes = [fila for fila in filas]
origen_droide = []

for p in personajes:
    if p["species"]=="Droid":
        origen_droide.append(Droides(p["name"], p["height"], p["mass"], p["birth_year"], p["gender"], p["homeworld"], p["films"]))

droides = [p for p in personajes if p["species"]=="Droid"]

for d in origen_droide:
    print(d)