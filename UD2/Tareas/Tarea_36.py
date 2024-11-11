## Escribir un programa que garde nunha variable o dicionario {'Euro':'€', ' Dollar':'$', ' Yen':'¥'}, 
# pregunte ao usuario por unha divisa e mostre o seu símbolo ou unha mensaxe de aviso se a divisa non está no dicionario. ##

if __name__ == "__main__":

    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

    entrada_usuario = input('De que divisa quieres obtener su símbolo?: ')


    for divisa, simbolo in divisas.items():
        if entrada_usuario.lower() == divisa.lower():
            print(simbolo)
            break
        else:
            print('Esa divisa non está disponible ou existe algún error tipográfico.')
            break
