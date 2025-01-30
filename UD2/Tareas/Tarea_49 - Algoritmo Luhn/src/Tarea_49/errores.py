class error_numero_caracteres(Exception):
    def __str__(self):
        return "Los números de tarjeta de longitud 1 o menor son considerados inválidos."

class error_de_formato(Exception):
    def __str__(self):
        return "El número de tarjeta debe contener únicamente caracteres numéricos (0..9)."
    
class error_algoritmo_luhn(Exception):
    def __init__(self,numero):
        self.numero = numero
    def __str__(self):
        return f"El número de tarjeta {self.numero} no es correcto. Introduzca un número de tarjeta válido."