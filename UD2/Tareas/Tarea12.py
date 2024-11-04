# Escribir un programa que pida ao usuario dous números e mostre por pantalla a súa división. 
# Se o divisor é cero debes amosar unha mensaxe de erro, do estilo non se pode dividir <n> por 0.

if __name__ == '__main__':
    num_1 = input('Introduza o primeiro número: ')
    num_2 = input('Introduza o segundo número: ')

    if int(num_2) == 0: 
        print('ERRO: Non se pode dividir', num_1,' entre 0')
    else: 
        print('Resultado: ', int(num_1)/int(num_2))