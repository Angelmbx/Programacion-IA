from Tarea_50.errores import error_algoritmo_luhn
from Tarea_50.algoritmo_luhn import algoritmo_luhn


class Usuario:
    def __init__(self, nombre, username, password, tarjeta=None):
        self.nombre = nombre
        self.username = username
        self.password = password
        self._tarjeta = None
        self.tarjeta = tarjeta

    def mostrar_usuario(self):
        return f"Nombre: {self.nombre}, Username: {self.username}, Password: {self.password}, Tarjeta: {self.tarjeta}"


    @property
    def tarjeta(self):
        return self._tarjeta

    @tarjeta.setter
    def tarjeta(self, numero):
        if numero is None or algoritmo_luhn(numero): 
            self._tarjeta = numero
        else:
            raise error_algoritmo_luhn(numero)

    