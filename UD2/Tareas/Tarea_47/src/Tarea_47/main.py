# # Unha inmobiliaria dunha cidade manexa unha lista de inmobles como a seguinte:

# # [{'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe':  True, 'zona': 'A'},
# # {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe':  True, 'zona': ' B'},
# # {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe':  False, 'zona': 'A'},
# # {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe':  True, 'zona': ' B'},
# # {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe':  False, 'zona': 'A'}]

# # Construír unha función que permita facer a procura de inmobles en función dun orzamento dado. A función recibirá como entrada a lista de inmobles
# #  e un prezo, e devolverá outra lista cos inmobles cuxo prezo sexa menor ou igual que o dado. Os inmobles da lista que se devolva deben incorporar
# #  un novo atributo do a cada dicionario co prezo do inmoble, onde o prezo dun inmoble calcúlase coa seguinte fórmula en función da zona:

# #     Zona A: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100)
# #     Zona  B: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100) * 1.5


def calcular_prezo(piso):
    metros = piso['metros']
    habitacions = piso['habitacións']
    garaxe = 15000 if piso['garaxe'] else 0
    antiguedade = 2025 - piso['ano']
    zona_factor = 1.5 if piso['zona'] == 'B' else 1

    return (metros * 1000 + habitacions * 5000 + garaxe) * (1 - antiguedade / 100) * zona_factor


def buscador_de_pisos(lista, presupuesto):

    pisos_disponibles = list(filter(lambda piso: calcular_prezo(piso) <= presupuesto, lista))
    
    for piso in pisos_disponibles:
        piso['prezo'] = calcular_prezo(piso)
    
    return pisos_disponibles



if __name__ == '__main__':
    
    lista_pisos = [
        {'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe': True, 'zona': 'A'},
        {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe': True, 'zona': ' B'},
        {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe': False, 'zona': 'A'},
        {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe': True, 'zona': ' B'},
        {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe': False, 'zona': 'A'}
    ]
    
    presupuesto = 80000
    pisos_disponibles = buscador_de_pisos(lista_pisos, presupuesto)
    
    print("Pisos disponibles:")
    for piso in pisos_disponibles:
        print(piso)
