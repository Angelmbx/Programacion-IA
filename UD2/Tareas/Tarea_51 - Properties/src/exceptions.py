
class velocidad_negativa(Exception):
    
    def __init__(self, new_vel):
        self.new_vel = new_vel
    def __str__(self):
        return f"La velocidad no puede tener un valor negativo. ({self.new_vel})"
    
class disminuir_total_kms(Exception):

    def __init__(self, total_kms, new_kms):
        self.total_kms = total_kms
        self.new_kms = new_kms

    def __str__(self):
        return f"El kilometraje no puede decrecer. (Valor previo: {self.total_kms} Intento de nuevo valor: {self.new_kms})"
