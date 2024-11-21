# Similar a exercicios anteriores, podes copiar o feito nesa parte e continuar ampliando:
# Escribir unha función que calcule a área dun círculo e outra que calcule o volume dun cilindro usando a primeira función.
# A area do círculo é pi*r**2                      O volume do cilindro é  pi*r**2 * h
# Xera test uniatarios, primeiro para a función que calcula a area do circulo, e logo para o volume do cilindro.

from math import pi

def area_circulo(r):
    if not isinstance(r, (int, float)):
        raise TypeError('O radio ten que ser un valor numérico')
    if r < 0:
        raise ValueError('O radio non pode ser negativo')
    return round(pi * r**2, 2)

def volumen_cilindro(r, h):
    if not isinstance(r, (int, float)):
        raise TypeError('O radio ten que ser un valor numérico')
    if not isinstance(h, (int, float)):
        raise TypeError('A altura ten que ser un valor numérico')
    if r < 0 or h < 0:
        raise ValueError('O radio e a altura non poden ser negativos')
    return round(area_circulo(r) * h, 2)



if __name__ == "__main__":
    try:
        radio_circulo = float(input('Introduza o radio do circulo: '))
        radio_cilindro = float(input('Introduza o radio do cilindro: '))
        altura_cilindro = float(input('Introduza a altura do cilindro: '))

        print(f'Área do círculo: {area_circulo(radio_circulo):.2f}')
        print(f'Volume do cilindro: {volumen_cilindro(radio_cilindro, altura_cilindro):.2f}')
    except (ValueError, TypeError) as e:
        print(f"Erro: {e}")
