from probatest.main import suma


def test_1mas0():
    assert suma(1,0) == 1
    assert suma(0,1) == 1
    # si todos los assert estan bien dentro de la misma funcion devuelve True, si uno falla devuelve False

def test_outro():
    assert suma(5,4) == 9
    #assert suma(3,45) == 1
    