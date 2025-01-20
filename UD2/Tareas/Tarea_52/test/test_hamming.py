import pytest
from src.celula import Celula
from src.utils import distancia_Hamming_calculator
from src.exceptions import longitud_cadenas_error

def test_distancia_hamming_valida():
    cadena1 = "GAGCCTACTAACGGGAT"
    cadena2 = "CATCGTAATGACGGCCT"
    assert distancia_Hamming_calculator(cadena1, cadena2) == f'Longitud de distancia Hamming: {7}'

def test_cadenas_longitudes_diferentes():
    cadena1 = "GAGCCTACTAACGGGAT"
    cadena2 = "CATCCGGCC"
    with pytest.raises(longitud_cadenas_error):
        distancia_Hamming_calculator(cadena1, cadena2)

def test_celula_metodo_sub():
    c1 = Celula("GAGCCTACTAACGGGAT")
    c2 = Celula("CATCGTAATGACGGCCT")
    assert c1 - c2 == f'Longitud de distancia Hamming: {7}'

def test_cadenas_iguales():
    c1 = Celula("GAGCCTACTAACGGGAT")
    c2 = Celula("GAGCCTACTAACGGGAT")
    assert c1 - c2 == f'Longitud de distancia Hamming: {0}'

def test_longitudes_diferentes_con_sub():
    c1 = Celula("GAGCCTACTAACGGGAT")
    c2 = Celula("CATCGTAATGACGGC")
    with pytest.raises(longitud_cadenas_error):
        c1 - c2
