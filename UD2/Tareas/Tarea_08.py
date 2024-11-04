## Os teléfonos dunha empresa teñen o seguinte formato prefixo-número- extension onde o prefixo é o código do país +34, 
# e a extensión ten dous díxitos (por exemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato e mostre por pantalla o número de teléfono sen o prefixo e a extensión.

if __name__ == '__main__':
    telefono_completo = input('Introduza o seu número de telf. indicando prefixo, número e extensión (por exemplo +34-913724710-56): ')

    solo_telefono = telefono_completo[4:-3]

    print(solo_telefono)
