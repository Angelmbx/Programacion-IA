## Escribir un programa que almacene a cadea de caracteres contrasinal nunha variable, pregunte ao usuario polo contrasinal ata que 
# introduza o contrasinal correcto. Parecido a un dos anteriores,  pero neste caso se trata de conseguir mediante un bucle a repetición 
# ata acertar co contrasinal

if __name__ == '__main__':
    contrasinal = 'AFS55xrjT'

    while True:
        entrada_usuario = input("Introduza o seu contrasinal: ")

        if entrada_usuario == contrasinal:
            print('Contrasinal correcto')
            break
        elif entrada_usuario == '*':
            print('Pechando programa.... Pechado.')
            break
        else:
            print('Contrasinal incorrecto, inténteo de novo ou escriba "*" para sair')

