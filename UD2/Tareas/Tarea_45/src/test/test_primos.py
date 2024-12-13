import pytest
from Tarea_45.main import primos_checker

def test_variado():
    lista = [2, 10, 4, 7, 12, 13, 20]
    assert primos_checker(lista) == [2, 7, 13]

def test_todo_primos():
    lista = [2, 3, 5, 7, 11]
    assert primos_checker(lista) == [2, 3, 5, 7, 11]

def test_sen_primos():
    lista = [1, 4, 6, 8, 9, 10]
    assert primos_checker(lista) == []

def test_con_negativos_e_cero():
    lista = [-5, 0, 1, 2, 3]
    assert primos_checker(lista) == [2, 3]
