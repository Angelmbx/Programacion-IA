import pytest
from Tarea_47.main import calcular_prezo, buscador_de_pisos 

def test_calcular_prezo_zona_a():
    piso = {'ano': 2010, 'metros': 150, 'habitacións': 4, 'garaxe': True, 'zona': 'A'}
    # prezo = (150 * 1000 + 4 * 5000 + 15000) * (1 - (2025 - 2010)/100)
    # prezo = (150000 + 20000 + 15000) * (1 - 15/100)
    # prezo = 185000 * 0.85 = 157250
    assert calcular_prezo(piso) == 157250

def test_calcular_prezo_zona_b():
    piso = {'ano': 2015, 'metros': 80, 'habitacións': 3, 'garaxe': False, 'zona': 'B'}
    # prezo = (80 * 1000 + 3 * 5000 + 0) * (1 - (2025 - 2015)/100) * 1.5
    # prezo = (80000 + 15000) * (1 - 10/100) * 1.5
    # prezo = 95000 * 0.9 * 1.5 = 128250
    assert calcular_prezo(piso) == 128250


def test_buscador_sin_pisos_disponibles():
    lista_pisos = [
        {'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe': True, 'zona': 'A'},
        {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe': True, 'zona': 'B'}
    ]
    presupuesto = 50
    resultado = buscador_de_pisos(lista_pisos, presupuesto)
    assert len(resultado) == 0

def test_lista_vacia():
    lista_pisos = []
    presupuesto = 100000
    resultado = buscador_de_pisos(lista_pisos, presupuesto)
    assert resultado == []
