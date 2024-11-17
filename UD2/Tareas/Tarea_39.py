## Escribir un programa que cre un dicionario simulando unha cesta da compra. O programa debe preguntar o artigo e o seu prezo 
# e engadir o par ao dicionario, ata que o usuario decida terminar. Despois débese mostrar por pantalla a lista da compra e o 
# custo total ##

if __name__ == "__main__":

    cesta_compra = dict()

    while True:
        artigo = input('Introduza un novo artigo ou prema * para saír: ')
        if artigo == '*':
            break
        prezo = float(input('E o seu prezo: '))
        cesta_compra[artigo] = prezo


    print('LISTA DA COMPRA')
    for clave in cesta_compra.keys():
        print("{}  {}".format(clave, cesta_compra[clave]))
    