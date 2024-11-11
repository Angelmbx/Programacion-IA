## Escribir un programa que pregunte ao usuario os números gañadores da lotería primitiva, os almacene nunha lista 
# e logo os amose por pantalla ordenados de menor a maior. ##

if __name__ == "__main__":

    lista_numeros = list ()

    for i in range (0,6):
        numero = int(input('Introduza un a un os números gañadores da primitiva: '))
        lista_numeros.append(numero)

    lista_numeros.sort()
    
    print('--------')
    print('Os números gañadores ordeados de menor a maior foron: ')
    for numero in lista_numeros:
        print(numero)


