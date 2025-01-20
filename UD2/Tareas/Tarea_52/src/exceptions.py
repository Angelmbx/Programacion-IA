class longitud_cadenas_error(Exception):
    
    def __init__(self, cadena1, cadena2):
        self.cadena1 = cadena1
        self.cadena2 = cadena2
    def __str__(self):
        return f"Las cadenas de adn deben tener la misma longitud. Cadena 1: {self.cadena1}, Cadena 2: {self.cadena2} "