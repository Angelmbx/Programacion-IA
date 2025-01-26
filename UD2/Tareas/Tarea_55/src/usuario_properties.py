from dataclasses import dataclass, field
from src.algoritmo_luhn import algoritmo_luhn
from src.errores import error_algoritmo_luhn

# nome, apelidos, o nome completo (que se obtén de xuntar o nome e os apelidos) 
# un nome de usuario, un contrasinal e un número de tarxeta. O número de tarxeta segue a formula de Luhn.

@dataclass
class Usuario_properties():
    nombre : str
    apellidos : str
    nombre_completo : str = field(init=False, repr=False)
    username : str
    password : str
    _tarjeta : str = field(default=None, repr=False, init=False)
    
    def __post_init__ (self):
        self.nombre_completo = f"{self.nombre} {self.apellidos}"
    
    @property
    def tarjeta(self):
        return self._tarjeta
    
    def set_tarjeta(self, numero):
        if algoritmo_luhn(numero):
            self._tarjeta = numero
        else:
            raise error_algoritmo_luhn(numero)
    
    tarjeta = property(tarjeta, set_tarjeta)