from src.exceptions import velocidad_negativa, disminuir_total_kms

class Vehiculo:

    def __init__(self, max_vel, total_kms):
        self.max_vel = max_vel
        self._total_kms = 0
        self.total_kms = total_kms


    def mostrar_vehiculo(self):
        return f"Velocidad máxima: {self.max_vel}, kilometraje: {self.total_kms}"
    
    @property
    def max_vel(self):
        return self._max_vel

    @max_vel.setter
    def max_vel(self, new_vel):
        if new_vel < 0:
            raise velocidad_negativa(new_vel)
        else:
            self._max_vel = new_vel


    @property
    def total_kms(self):
        return self._total_kms

    @total_kms.setter
    def total_kms(self, new_kms):
        if self._total_kms > new_kms :
            raise disminuir_total_kms(self._total_kms, new_kms)
        else:
            self._total_kms = new_kms
