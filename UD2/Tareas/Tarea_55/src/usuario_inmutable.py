from dataclasses import dataclass, field
from src.algoritmo_luhn import algoritmo_luhn
from src.errores import error_algoritmo_luhn

@dataclass(frozen=True)
class Usuario():
    nombre : str
    apellidos : str
    username : str
    password : str
    tarjeta : str = None
    nombre_completo: str = field(init=False, repr=False)
    def __post_init__(self):
        # al ser la clase inmutable, es necesario el object.__setattr__() para modificar uno de lo atributos 
        object.__setattr__(self, "Nombre_completo: ", f"{self.nombre} {self.apellidos}")
        # cuando se introduce un numero de tarjeta, es cuando se valida.
        if self.tarjeta is not None and not algoritmo_luhn(self.tarjeta):
            raise error_algoritmo_luhn(self.tarjeta)
    

    