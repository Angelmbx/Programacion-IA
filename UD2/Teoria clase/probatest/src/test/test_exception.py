from probatest.main import suma
import pytest

def test_suma_str():
    with pytest.raises(TypeError):
        suma ("a", 1)