from tarea41.main import suma
import pytest


def test_enteiro_positivo():
    assert suma(5) == 15

def test_negativo():
    with pytest.raises(ValueError):
        suma(-5)
    
def test_float():
    with pytest.raises(TypeError):
        suma(8.75)