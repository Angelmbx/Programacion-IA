class longitud_cadenas_error(Exception):
    
    def __init__(self, cadena1, cadena2):
        self.cadena1 = cadena1
        self.cadena2 = cadena2
    def __str__(self):
        return f"Las cadenas de adn deben tener la misma longitud. Longitud Cadena 1: {len(self.cadena1)}, Cadena 2: {len(self.cadena2)} "