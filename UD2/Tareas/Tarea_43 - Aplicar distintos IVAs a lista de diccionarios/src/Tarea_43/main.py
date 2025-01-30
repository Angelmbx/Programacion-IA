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

def total(cesta):
        prezo_final = 0
        ive_total = 0
        desconto_total = 0

        for artigo in cesta:
            prezo_sen_ive = artigo["prezo sen ive"]
            prezo_ive = artigo["tipo ive"]
            if artigo["desconto"] == None:
                desconto_aplicado = 0
            else:
                desconto_aplicado = artigo["desconto"] 

            prezo_final += prezo_ive - desconto_aplicado
            ive_total += prezo_ive - prezo_sen_ive
            desconto_total += desconto_aplicado

        return {
        "total_a_pagar": round(prezo_final, 2),
        "total_ive": round(ive_total, 2),
        "total_descontos": round(desconto_total, 2)
     }

if __name__ == "__main__":
    
    lista_compra = [
        {"produto": "mazás", "prezo sen ive": 1.15, "tipo ive": aplicacion_21_ive(1.15), "desconto": None},
        {"produto": "queixo", "prezo sen ive": 2.88, "tipo ive": aplicacion_21_ive(2.88), "desconto": desconto(aplicacion_21_ive(2.88))},
        {"produto": "tomates", "prezo sen ive": 1.40,"tipo ive": aplicacion_4_ive(1.40), "desconto": None},
        {"produto": "Pack de leite", "prezo sen ive": 5.60,"tipo ive": aplicacion_21_ive(5.60), "desconto": desconto(aplicacion_21_ive(5.60))}
    ]

    resultados = dict()

    resultados = total(lista_compra)

    print(f"Total a pagar: {resultados['total_a_pagar']}€")
    print(f"Total IVE: {resultados['total_ive']}€")
    print(f"Total Descontos: {resultados['total_descontos']}€")

