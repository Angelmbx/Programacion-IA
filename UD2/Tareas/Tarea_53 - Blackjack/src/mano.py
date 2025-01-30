from src.carta import Carta

class Mano:
    
    def __init__(self):
        self.carta1 = comprobador_de_ases(Carta())
        self.carta2 = comprobador_de_ases(Carta())
        self.puntuacion = self.carta1.valor + self.carta2.valor

    def añadir_carta(self):
        self.nueva_carta = comprobador_de_ases(Carta())
        self.puntuacion += self.nueva_carta.valor


def comprobador_de_ases(n):
    if n.figura == "As":
        while True:
            decision = input("Has recibido un As, quieres que valga 1 ó 11?: ")
            if decision.strip() == "11":
                n.valor = 11
                break
            elif decision.strip() == "1":
                n.valor = 1
                break
            else:
                print("Respuesta incorrecta. Debes asignarle un valor 1 o 11. ")
    
    return n