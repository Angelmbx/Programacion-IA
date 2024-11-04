## Para tributar un determinado imposto débese ser maior de 16 anos e ter uns ingresos iguais ou superiores a 1000 € mensuais. 
## Escribir un programa que pregunte ao usuario a súa idade e os seus ingresos mensuais e mostre por pantalla se o usuario ten que tributar ou non.

if __name__ == '__main__':
    idade = input('Introduza a súa idade: ')
    ingresos = input('Introduza os seus ingresos mensuais: ')

    if int(idade) > 16 and int(ingresos) >= 1000:
        print('Vostede ten que tributar')
    else:
        print('Vostede non ten que tributar')