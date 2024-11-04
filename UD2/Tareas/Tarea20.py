## Escribir un programa que lea un enteiro positivo, n, introducido polo usuario e despois mostre en pantalla
#  a suma de todos os enteiros desde 1 ata n. ##

if __name__ == '__main__':
    numero = int(input('Introduza un numero: '))
    index = 1
    sumatorio = 1

    while index <= numero:
        sumatorio = index + (index + 1)
        index += 1 
    
    print(sumatorio)



