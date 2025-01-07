import pytest

from Tarea_46.main import pares_checker  

def test_lista_todos_pares():
    assert pares_checker([2, 4, 6, 8, 10]) == True

def test_lista_con_impares():
    assert pares_checker([2, 4, 5]) == False

def test_lista_vacia():
    assert pares_checker([]) == "La lista está vacía" 

def test_argumento_no_es_lista():
    assert pares_checker("Esto no es una lista") == "Se esperaba una lista"
 
