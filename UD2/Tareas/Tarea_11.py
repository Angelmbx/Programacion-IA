## Escribir un programa que almacene a cadea de caracteres contrasinal nunha variable, 
# pregunte ao usuario polo contrasinal e imprima por pantalla se o contrasinal introducido polo usuario coincide 
# coa gardada na variable sen ter en conta maiúsculas e minúsculas.

if __name__ == '__main__':
    contrasinal = 'AFS55xrjT'

    input = input("Introduza o seu contrasinal: ")

    if input.lower() == contrasinal.lower():
        print('Contrasinal correcto')
    else:
        print('Contrasinal incorrecto, inténteo de novo.')

