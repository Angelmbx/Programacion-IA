from Tarea_42.main import area_circulo
import pytest

def test_numero_entero():
    assert area_circulo(4) == 50.27

def test_negativo():
    with pytest.raises(ValueError):
        area_circulo(-4)
    