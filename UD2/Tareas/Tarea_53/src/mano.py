from src import carta

class Mano:
    
    def __init__(self):
        self.carta1 = carta.Carta()
        self.carta2 = carta.Carta()
        self.puntuacion = self.carta1.valor + self.carta2.valor