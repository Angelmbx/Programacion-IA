from errores import error_algoritmo_luhn, error_de_formato, error_numero_caracteres


def algoritmo_luhn(numero):

    # Eliminar espacios
    numero = numero.replace(" ", "")  

    if len(numero) < 2:
        raise error_numero_caracteres
    if not numero.isdigit():
        raise error_de_formato
    
    # Invertir número
    numero = numero[::-1]
    suma = 0  

    for index in range(len(numero)):
        digito = int(numero[index]) # convierto cada numero de la cadena a entero
        
        if index % 2 == 1:  # Como se empieza a contar en 0, se multiplican * 2 las posiciones cuyo índice sea un número impare (índice 1 es la 2ª posicion, índice 3 la 4ª, etc.)
            digito *= 2
            if digito > 9: 
                digito -= 9

        suma += digito

   
    return suma % 10 == 0



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
