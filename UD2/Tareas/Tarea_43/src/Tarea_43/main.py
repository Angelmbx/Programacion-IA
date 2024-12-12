## Para esta tarefa imos a precisar:
# - Unha función que aplique un 21% de IVE a unha cantidade
# - Unha función que aplique un 4% de IVE a unha cantidade
# - Unha función que aplique un 10%  de desconto a unha cantidade.

# Finalmente vas a ter unha lista coa lista da compra. Para elemento da lista será un dicionario onde haberá:
# - prezo do produto sen IVE
# - unha función que aplica o desconto... ou None en caso de non ter desconto
# - unha función que calcule o IVE do produto

# Crearás unha función que colla unha cesta da compra e nos devolve o total a pagar, o IVE da compra e máis a cantidade obtida de aplicar os descontos.
# Xera os tes unitarios correspondentes.
##



def aplicacion_21_ive(produto_sen_ive):
    return produto_sen_ive * 1.21

def aplicacion_4_ive(produto_sen_ive):
    return produto_sen_ive * 1.04

def desconto(prezo):
    return prezo * 0.1

if __name__ == "__main__":
    
    lista_compra = [
        {"produto": "mazás", "prezo sen ive": 1.15, "tipo ive": aplicacion_21_ive(1.15), "desconto": None},
        {"produto": "queixo", "prezo sen ive": 2.88, "tipo ive": aplicacion_21_ive(2.88), "desconto": desconto(aplicacion_21_ive(2.88))},
        {"produto": "tomates", "prezo sen ive": 1.40,"tipo ive": aplicacion_4_ive(1.40), "desconto": None}
    ]

    def total(cesta):
        return 