## Escribir un programa que pregunte ao usuario polo número de horas traballadas e o custo por hora.
## Despois debe mostrar por pantalla a paga que lle corresponde.

if __name__ == '__main__':
    horas = input('Ola, indique o número de horas traballadas: ')
    custo = input('Agora indique o custo por hora: ')

    paga = int(horas) * int(custo)
    
    print('Correspóndenche ', paga,' euros')