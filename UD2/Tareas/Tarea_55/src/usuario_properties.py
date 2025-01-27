from dataclasses import dataclass, field
from src.algoritmo_luhn import algoritmo_luhn
from src.errores import error_algoritmo_luhn


@dataclass
class Usuario_properties():
    nombre : str = field(repr=False)
    apellidos : str = field(repr=False)
    nombre_completo : str = field(init=False, repr=True)
    username : str
    password : str
    _tarjeta : str = None
    
    def __post_init__ (self):
        self.nombre_completo = f"{self.nombre} {self.apellidos}"
        if not algoritmo_luhn(self._tarjeta):
            raise error_algoritmo_luhn(self._tarjeta) 

    @property
    def tarjeta(self):
        return self._tarjeta
    
    def set_tarjeta(self, numero):
        self._tarjeta = numero

    tarjeta = property(tarjeta, set_tarjeta)