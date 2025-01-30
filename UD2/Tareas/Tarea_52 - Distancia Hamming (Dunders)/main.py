from src.utils import distancia_Hamming_calculator
from src.celula import Celula
from src.exceptions import longitud_cadenas_error

if __name__ == '__main__':
    
    c1 = Celula("GTGCCTACTAACGGGAT")
    c2 = Celula("AAAAATACTAACGGGAT")

    try:
        print(distancia_Hamming_calculator(c1.cadena, c2.cadena))
    except longitud_cadenas_error as e:
        print(e)


    # Ampliación, redefiniendo el método __sub__ (ver clase Célula)
    try:
         print(c1-c2)
    except longitud_cadenas_error as e:
         print(e)