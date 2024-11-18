## Partindo dun programa que indique se un número é primo ou non.
#   Facer un programa no que o mensaxe que indica se o numero é primo o non sexa posto por unha vaca. 
#   Para iso podes usar a librería cowsay.
#   Crea un environment de python có modulo venv. Instala dentro do environment o paquete cowsay.
#   Fai o programa é probao dentro do environment.
#   Crea un ficheiro environment.yml para crear unha contorna de conda, a versión de python que queiras. 
#   Indica que no environment que queres que te instale o paquete cowsay (non vai a estar no channel anaconda)
#   Traballa co environment
#   Crea un proxecto mediante uv, coa versión de python 3.11.
#   Agrega a librería cowsay e executa o programa dentro do environment creado por uv.
# ##

import cowsay

if __name__ == "__main__": 
    numero = int(input("Introduza un número enteiro: "))
    numero_primo = True
    index = 1

    for index in range(2, numero//2+1):
        if numero % index == 0:
            numero_primo = False
            break
            
    if numero_primo:
        cowsay.cow('O número introducido é primo')
    else:
        cowsay.cow('O número introducido NON é primo')