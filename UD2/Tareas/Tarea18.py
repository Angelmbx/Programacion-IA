## Escribir un programa que pida ao usuario un número enteiro positivo e mostre por pantalla todos os números impares desde 1 ata ese número separados por comas.##

if __name__ == '__main__':
    numero = int(input('Introduza un numero enteiro: '))
    index = 1

    print('Números impares dende 1 ata',numero,':' )
    
    while index <= numero:
        if index % 2 != 0:
            print(index)
        index += 1
    
    