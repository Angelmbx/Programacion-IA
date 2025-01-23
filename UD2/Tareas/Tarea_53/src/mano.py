from src.carta import Carta

class Mano:
    
    def __init__(self):
        self.carta1 = Carta()
        self.carta2 = Carta()
        self.puntuacion = self.carta1.valor + self.carta2.valor

    def añadir_carta(self):
        self.nueva_carta = Carta()
        self.puntuacion += self.nueva_carta.valor
