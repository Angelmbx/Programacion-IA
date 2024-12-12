## Escribe unha función que reciba coma parámetros unha lista e mais unha función,
# e devolva unha nova lista onde cada elemento é o resultado de aplicares a función ao elemento orixinal da lista. ##


def funcion(lista, f):
    return [f(elemento) for elemento in lista]  

def doble(a):
        return a * 2

if __name__ == '__main__':
    lista = [10, 15, 25, 40]
    
    print(funcion(lista, doble))  
