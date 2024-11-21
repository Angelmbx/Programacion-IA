from Tarea_42.main import volumen_cilindro
import pytest


def test_numero_entero():
    assert volumen_cilindro(4,10) == 502.70

def test_radio_non_intfloat():
    with pytest.raises(TypeError):
        volumen_cilindro("Jaimito", 6)

def test_altura_non_intfloat():
    with pytest.raises(TypeError):
        volumen_cilindro(4, "Saudos")

def test_radio_ou_altura_negativos():
    with pytest.raises(ValueError):
        volumen_cilindro(12, -50)
    