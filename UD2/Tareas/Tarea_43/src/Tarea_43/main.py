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



def aplicacion_21_ive(producto_sen_ive):
    return producto_sen_ive * 1.21

def aplicacion_10_ive(producto_sen_ive):
    return producto_sen_ive * 1.10

def aplicacion_4_ive(producto_sen_ive):
    return producto_sen_ive * 1.04



if __name__ == "__main__":
    main()
