## Escribir un programa que pregunte o nome do usuario na consola e despois de que o usuario introdúzao mostre por pantalla
# <usuario> ten < n> letras, onde  é o nome de usuario en maiúsculas e < n> é o número de letras que teñen o nome.

if __name__ == '__main__':
    nome = input('Introduza o seu nome: ')

    print(nome.upper(), 'ten ', len(nome), 'letras')