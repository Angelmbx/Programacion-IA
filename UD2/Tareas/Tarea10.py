## Escribir un programa que pregunte ao usuario a súa idade e mostre por pantalla se é maior de idade ou non. ##

if __name__ == '__main__':
    idade = input('Indique a súa idade: ')

    if int(idade) < 18:
        print('Vostede é menor de idade')
    else:
        print(' Vostede é maior de idade')