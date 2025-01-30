##Escribe un programa onde declares unha clase vehiculo con velocidade máxima e kilometraxe coma atributos.
# Controla que a velocidade máxima non pode ser negativa, e que o kilometraxe nunca pode descender.
# Implementa a transformación do obxecto vehiculo a string. Fai os test correspondentes ##

from src.vehiculo import Vehiculo
from src.exceptions import velocidad_negativa, disminuir_total_kms


if __name__ == "__main__":
    
    try:
        renault = Vehiculo(200, 100)
        print(renault.mostrar_vehiculo())

        #renault.max_vel = -30
        renault.total_kms = 20

    except velocidad_negativa as negative_speed_error:
        print(negative_speed_error)
    except disminuir_total_kms as decrease_kms_error:
        print(decrease_kms_error)

