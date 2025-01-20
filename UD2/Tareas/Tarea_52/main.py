from src.utils import distancia_Hamming_calculator
from src.celula import Celula


if __name__ == '__main__':
    
    c1 = Celula("GAGCCTACTAACGGGAT")
    c2 = Celula("CATCGTAATGACGGCCT")

    print(distancia_Hamming_calculator(c1.cadena, c2.cadena))

    # Ampliación, redefiniendo el método __sub__ (ver clase Célula)
    print(c1-c2)