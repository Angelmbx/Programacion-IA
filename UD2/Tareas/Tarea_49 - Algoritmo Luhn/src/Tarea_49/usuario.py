from Tarea_49.errores import error_algoritmo_luhn, error_de_formato, error_numero_caracteres
from Tarea_49.algoritmo_luhn import algoritmo_luhn


class Usuario:
    def __init__(self, nombre, username, password, tarjeta = None):
        self.nombre = nombre
        self.username = username
        self.password = password
        if algoritmo_luhn(tarjeta):
            self.tarjeta = tarjeta
        else:
            raise error_algoritmo_luhn(tarjeta)
            
    def mostrar_usuario(self):
        return f"Nombre: {self.nombre}, Username: {self.username}, Password: {self.password}, Tarjeta: {self.tarjeta}"
