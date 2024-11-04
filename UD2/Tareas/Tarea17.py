## Escribir un programa que pregunte ao usuario a súa idade 
# e mostre por pantalla todos os anos que cumpriu (desde 1 ata a súa idade). ##

if __name__ == '__main__':
    idade = int(input('Indique a súa idade: '))
    ano = 1
    print('Vostede cumpriu todos estes anos: ')
   
    while ano <= idade:
        print(ano)
        ano += 1