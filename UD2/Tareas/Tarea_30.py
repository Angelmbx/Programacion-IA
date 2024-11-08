## Escribir unha función que calcule a área dun círculo e outra que calcule o volume dun cilindro usando a primeira función.
# A area do círculo é pi*r**2
# O volume do cilindro é  pi*r**2 * h ##

from math import pi

if __name__ == "__main__":
    radio_circulo = float(input('Introduza o radio do circulo: '))
    radio_cilindro = float(input('Introduza o radio do cilindro: '))
    altura_cilindro = float(input('Introduza a altura do cilindro: '))

    def radio_circulo_calculator(r):
        return pi * r ** 2
    
    def radio_cilindro_calculator(r,h):
        return radio_circulo_calculator(r) * h 
    
    print(f'Área do círculo: {radio_circulo_calculator(radio_circulo)}')
    print(f'Área do cilindro: {radio_cilindro_calculator(radio_cilindro, altura_cilindro)}')