## Escribir un programa que pida ao usuario un número enteiro positivo e mostre por pantalla a conta atrás 
# desde ese número ata cero separados por comas. ##

if __name__ == '__main__':
    numero = int(input('Introduza un número enteiro: '))
    lista_numeros = list()

    while numero >= 0:
        lista_numeros.append(numero)
        numero -= 1
    
    print(lista_numeros)