
import pytest
from Tarea_44.main import funcion, doble

def test_doble():
    assert doble(2) == 4
    assert doble(0) == 0
    assert doble(-5) == -10

def test_funcion():
    lista = [10, 15, 25, 40]
    resultado = funcion(lista, doble)
    assert resultado == [20, 30, 50, 80]  

    lista_negativos = [-2, -4, -6]
    resultado_negativos = funcion(lista_negativos, doble)
    assert resultado_negativos == [-4, -8, -12] 
