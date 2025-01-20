from src.exceptions import longitud_cadenas_error

def distancia_Hamming_calculator(cadena1, cadena2):

    if len(cadena1) != len(cadena2):
        raise longitud_cadenas_error

    else: 

        diferencias = 0

        for i,j in zip(cadena1,cadena2):
                if i != j:
                    diferencias += 1
        
        return diferencias