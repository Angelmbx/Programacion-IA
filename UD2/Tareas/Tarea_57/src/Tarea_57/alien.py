def generador_de_alienigenas_en_serie(posiciones, total_aliens):

    for posicion in posiciones:
        Alien(posicion[0], posicion[1], total_aliens)

    return total_aliens


def contador_de_alienigenas(lista_alienigenas):
        return f"Se crearon un total de {len(lista_alienigenas)} alienígenas."


class Alien:
    def __init__(self, x, y, total):
        self.x = x
        self.y = y
        self.salud = 3
        total = total.append(self)

    def hit(self, rival, daño= 1):
        rival.salud -= daño

    def is_alive(self):
        if self.salud <= 0:
            return False
        
        return True
    
    def teletransportacion(self, x, y):
        self.x = x
        self.y = y

        return (self.x, self.y)

    def deteccion_colisiones(self, objeto):
        pass

    