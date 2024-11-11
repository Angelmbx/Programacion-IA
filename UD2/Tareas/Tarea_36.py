## Escribir un programa que garde nunha variable o dicionario {'Euro':'€', ' Dollar':'$', ' Yen':'¥'}, 
# pregunte ao usuario por unha divisa e mostre o seu símbolo ou unha mensaxe de aviso se a divisa non está no dicionario. ##

if __name__ == "__main__":

    divisas = {'euro':'€', 'dollar':'$', 'yen':'¥'}

    entrada_usuario = input('De que divisa quieres obtener su símbolo?: ').lower()

    simbolo = divisas.get(entrada_usuario)
    
    if simbolo:
        print(f'O símbolo de {entrada_usuario} é {simbolo}.')
    else:
        print(f'A divisa "{entrada_usuario}" non se atopa no rexistro.')
