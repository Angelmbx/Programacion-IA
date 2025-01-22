from src import mano

class Jugador:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.mano = mano.Mano()
        
    