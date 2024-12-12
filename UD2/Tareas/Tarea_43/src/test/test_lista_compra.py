import pytest
from Tarea_43.main import aplicacion_21_ive, aplicacion_4_ive, desconto, total

def test_aplicacion_21_ive():
    assert aplicacion_21_ive(100) == 121.0
    assert aplicacion_21_ive(0) == 0.0
    assert round(aplicacion_21_ive(1.15), 2) == 1.39


def test_aplicacion_4_ive():
    assert aplicacion_4_ive(100) == 104.0
    assert aplicacion_4_ive(0) == 0.0
    assert round(aplicacion_4_ive(1.40), 2) == 1.46

def test_desconto():
    assert desconto(100) == 10.0
    assert desconto(0) == 0.0
    assert round(desconto(121), 2) == 12.1
