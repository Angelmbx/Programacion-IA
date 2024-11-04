## Os alumnos dun curso dividíronse en dous grupos A e  B de acordo ao sexo e o nome. 
# O grupo A esta formado polas mulleres cun nome anterior á  M e os homes cun nome posterior á  N e o grupo  B polo resto. 
# Escribir un programa que pregunte ao usuario o seu nome e sexo, e mostre por pantalla o grupo que lle corresponde.

if __name__ == '__main__':
    sexo = input('Indique se é home ou muller: ').lower()
    nome = input('Indique o seu nome: ').lower()

    if (sexo == 'muller' and nome[0] < 'm') or (sexo == 'home' and nome[0] < 'n'):
        print('Vostede está no grupo A')
    elif (sexo == 'muller' and nome[0] >= 'm') or (sexo == 'home' and nome[0] >= 'n'): 
        print('Vostede está no grupo B')
   