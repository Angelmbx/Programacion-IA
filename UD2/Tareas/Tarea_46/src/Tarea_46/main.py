## Fai unha función que nos indique se todos os elementos dunha lista son pares ou non. ##

def pares_checker(lista):
   
    if not isinstance(lista, list):  # Comprobación de si lo que se pasa es una lista
        return "Se esperaba una lista"

    if not lista:  # Comprobación de que la lista no esté vacía 
        return "La lista está vacía"

    pares = []

    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)

    return len(pares) == len(lista)


if __name__ == '__main__':

    lista = [12, 31, 203, 86, 10, 55, 17, 954]
    otra_lista = [2, 6, 8, 10]

    print(pares_checker(lista)) # False
    print(pares_checker(otra_lista)) # True