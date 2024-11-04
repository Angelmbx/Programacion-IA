## Escribir un programa que pida ao usuario que introduza unha frase na consola e mostre por pantalla a frase invertida.##

if __name__ == '__main__':
    frase = input('Introduza unha frase: ')

    frase_invertida = frase[::-1]

    print(frase_invertida)