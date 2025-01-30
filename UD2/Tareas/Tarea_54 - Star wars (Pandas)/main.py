#  Non seguinte ficheiro temos datos de personaxes de star wars:
#  por un lado temos os seres biolóxicos: que teñen as seguintes caracteristicas: name, height, mass, hair_color, skin_color, eye_color, birdth_year, sex, gender, homeworl, species, films
#  por outro teremos os droides, que teñen as seguintes características: name, height, mass,  birdth_year, gender, homeworl,  films 
#  O atributo films é unha lista separada por comas de películas.
#  Crea as clases que creas necesarias e asigna un tipo de dato correcto a cada atributo no momento da lectura.
# Implementa o método __str__
# Lee todas as liñas do ficheiro e crea unha instancia de un obxecto que represente ao personaxe e introduceos todos nunha lista.
# Imprime o conxunto completo de personaxes.
# Imprime só os personaxes que non sexan droids.

import pandas as pd
from src.seres_biologicos import Seres_biologicos
from src.droides import Droides

url = "UD2/Tareas/Tarea_54/starwars.csv"

archivo = pd.read_csv(url)

filas = archivo.to_dict(orient='records')

personajes = [fila for fila in filas]

origen_droide = []
origen_no_droide = []
todos = []
    
for p in personajes:
    if p["species"]=="Droid":
            
        droide = (Droides(p["name"], p["height"], p["mass"], p["birth_year"], p["gender"], p["homeworld"], p["films"]))
        origen_droide.append(droide)
        todos.append(droide)
    
    else:
        no_droide = (Seres_biologicos(p["name"],p["height"], p["mass"],p["hair_color"], p["skin_color"],p["eye_color"],p["birth_year"],p["sex"], p["gender"], p["homeworld"],p["species"], p["films"]))
        origen_no_droide.append(no_droide)
        todos.append(no_droide)


print("-"*55,"DROIDES","-"*55)   
for d in origen_droide:
    print(d)
    
print("-"*50,"TODOS LOS PERSONAJES","-"*50)   
for t in todos:
    print(t)
        