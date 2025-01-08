## Fai unha función que nos indique se todos os elementos dunha lista son pares ou non. ##

# def pares_checker(lista):
   
#     if not isinstance(lista, list):  # Comprobación de si lo que se pasa es una lista
#         return "Se esperaba una lista"

#     if not lista:  # Comprobación de que la lista no esté vacía 
#         return "La lista está vacía"

#     pares = []

#     for elemento in lista:
#         if elemento % 2 == 0:
#             pares.append(elemento)

#     return len(pares) == len(lista)

# ---------- CORRECCIÓN PARA USAR 'ALL' ---------------

def pares_checker(lista):

    if not isinstance(lista, list):
        return "Se esperaba una lista"
    if not lista:
        return "La lista está vacía"
    
    pares = (numero % 2 == 0 for numero in lista)
    if all(pares):
        return True
    else:
        return False

if __name__ == '__main__':

    lista = [12, 31, 203, 86, 10, 55, 17, 954]
    otra_lista = [2, 6, 8, 10]

    pares_checker(lista) 
    pares_checker(otra_lista) 