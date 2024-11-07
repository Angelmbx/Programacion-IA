## Escribir un programa que lea un  enteiro positivo,  n, introducido polo usuario e  despois  mostre en pantalla 
# a suma de todos vos  enteiros desde 1 ata  n. Para  facelo implementa  unha función que reciba un valor  n 
# e calcule ou resultado usando a  seguinte formula: resultado =  n * ( n +1)  / 2 ##

if __name__ == '__main__':

    numero = int(input('Introduza un número enteiro positivo: '))


    def suma(numero):
        return numero * ( numero +1)  / 2
       
    if numero < 0:
        print('O número debe ser positivo')
    else:
        print('Resultado: ', suma(numero))


 