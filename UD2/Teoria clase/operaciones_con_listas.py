#filtro:
lista = [{"x":10,"y":20},{"x":5,"y":5},{"x":20,"y":10}]
listaX = [elemento["x"] for elemento in lista if elemento["x"]>5]
    
#map:
def cuadrado(n):
    return n*n
lista = [0,1,2,3,4,5]
listaCuadrados = list(map(cuadrado,lista))

#lambda
def cuadrado(n):
    return n*n
lista = [0,1,2,3,4,5]
listaCuadrados = list(map(lambda x: x * x,lista))

#filtro con lambda
lista = [0,1,2,3,4,5]
listaPares = list(filter(lambda x: True if x % 2 == 0 else False,lista))

#all y any
lista = [0,2,12,22,30,4]
pares = (numero % 2 for numero in lista)
if all(pares):
    print("Todos son pares")
else:
    print("Non todo son pares")