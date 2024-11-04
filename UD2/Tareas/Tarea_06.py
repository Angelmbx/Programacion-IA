## Escribir un programa que pregunte o nome completo do usuario na consola e despois mostre por pantalla 
# o nome completo do usuario tres veces, unha con todas as letras minúsculas,
# outra con todas as letras maiúsculas e outra só coa primeira letra do nome e dos apelidos en maiúscula. 
# O usuario pode introducir o seu nome combinando maiúsculas e minúsculas como queira.


if __name__ == '__main__':
    nome = input('Introduza o seu nome completo: ')

    minusculas = nome.lower()
    maiusculas = nome.upper()
    iniciais = nome.title()

    print( minusculas,
           maiusculas,
            iniciais)