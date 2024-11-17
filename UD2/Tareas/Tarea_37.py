## Escribir un programa que pregunte ao usuario o seu nome, idade, dirección e teléfono e o garde nun dicionario. 
# Despois debe mostrar por pantalla a mensaxe  ten x anos, vive en <dir> e o seu número de teléfono é <num>. ##

if __name__ == "__main__":

    nome = input('Introduza o seu nome: ')
    idade = input('Introduza a súa idade: ')
    direccion = input('Introduza a dirección do seu domicilio: ')
    telf = input('Introduza o seu teléfono: ')

    datos_usuario = {"nome": nome, "idade": idade, "direccion": direccion, "telf": telf }

    print(f"{datos_usuario['nome']} ten {datos_usuario['idade']} anos, vive en {datos_usuario['direccion']} e o seu número de teléfono é {datos_usuario['telf']}.")