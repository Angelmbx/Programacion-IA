from src.utils import distancia_Hamming_calculator

class Celula:
    
    def __init__ (self, cadena):
        self.cadena = cadena

    def __sub__ (self, otra_celula):
        return distancia_Hamming_calculator(self.cadena, otra_celula.cadena)