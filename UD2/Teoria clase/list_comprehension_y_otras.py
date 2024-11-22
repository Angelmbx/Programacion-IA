### LIST COMPREHENSION ###


# creamos lista 
lista_numeros = list(range(10))
print(lista_numeros) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# elementos de la lista * 2
nova_lista =  []
for numero in lista_numeros:
    nova_lista.append(numero*2)
print(nova_lista)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# elementos * 10 utilizando list comprehension
nova_lista_2 = [numero*10 for numero in lista_numeros]
print(nova_lista_2) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]



# modificar lista utilizando list comprehension y pasándole una función
def f(numero):
    return numero * 5

nova_lista_3 = [f(numero) for numero in lista_numeros]
print(nova_lista_3) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]


# con lista de diccionarios
areas = []
lista = [{"x": 10, "y": 20}, {"x": 5, "y": 5}, {"x": 20, "y": 10}]
for elemento in lista:
    areas.append(elemento["x"]*elemento["y"]) # multiplica x por y en cada dict
print(areas) # [200, 25, 200]


areas = [elemento["x"]*elemento["y"] for elemento in lista]
print(areas) # [200, 25, 200]


# con string
letras = [letra.upper() for letra in "hola"]
print(letras) # ['H', 'O', 'L', 'A']


# tambien se puede filtrar

lista = [{"x":10,"y":20},{"x":5,"y":5},{"x":20,"y":10}]
listaX = [elemento["x"] for elemento in lista if elemento["x"]>5]
print(listaX) # solo elementos cuya x sea mayor que 5 = [10, 20]



### GENERATORS ###

generator_por_dos = (numero for numero in lista_numeros if numero %2 == 1)
print(generator_por_dos)
 
 # generator ocupa menos memoria que una list comprehension


 ### REDUCE ###

import functools
import operator

lista=[0,1,2,3,4,5]

suma = sum(lista)
print(f"Sum {suma}")

suma2 = functools.reduce(operator.add, lista)
print(f"Suma2 {suma2}")


def frara(x,y):
    return x*2 + y

suma3 = functools.reduce(frara, lista)
print(f"Suma3 {suma3}")


### ALL e ANY ###

lista = [0,2,12,22,30,4]
pares = (numero % 2 == 0 for numero in lista)
if all(pares):
  print(f"{lista} son todos pares") # [0,2,12,22,30,4]
else:
  print("Non todo son pares")

lista2 = [0,2,12,15,22,30,4]
pares = (numero % 2 == 0 for numero in lista2)
if all(pares):
  print(f"{lista} son todos pares")
else:
  print("Non todo son pares") # <-

  # Any funciona igual, solo que ALL busca un false y any busca un true