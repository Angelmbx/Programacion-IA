## Escribir un programa que lea un  enteiro positivo,  n, introducido polo usuario e  despois  mostre en pantalla
# a suma de todos vos  enteiros desde 1 ata  n. Para  facelo implementa  unha función que reciba un valor  
# n e calcule ou resultado usando a  seguinte formula: resultado =  n * ( n +1)  / 2
# Xera os test unitarios para a función feita. Chequea por exemplo, algun número do que sepas a solución, 
# que ocorre cando lle pasas un número negativo... corrixe a partires do resultado do test o necesario para que saia todo ben. ##


def suma(numero):
    if numero < 0: 
        raise ValueError('O número debe ser positivo')  
    if not isinstance(numero, int):  
        raise TypeError('Ten que ser un número enteiro')
    else:
        return numero * (numero + 1) / 2



if __name__ == "__main__":
    
    numero = int(input('Introduza un número enteiro positivo: '))

    resultado = suma(numero)

    print(f'Resultado: {resultado}')