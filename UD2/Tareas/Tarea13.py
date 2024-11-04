## Escribir un programa que pida ao usuario un número enteiro e mostre por pantalla se é par ou impar. ##

if __name__ == '__main__':
    numero = input('Introduza un número enteiro: ')
    
    if int(numero) % 2 == 0:
        print(numero, ' é par')
    else:
        print(numero, ' é impar')