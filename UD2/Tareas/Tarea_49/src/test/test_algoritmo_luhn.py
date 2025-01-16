import pytest
from Tarea_49.usuario import Usuario
from Tarea_49.algoritmo_luhn import algoritmo_luhn
from Tarea_49.errores import error_de_formato, error_numero_caracteres, error_algoritmo_luhn 

def test_algoritmo_luhn():
    # Tarjeta valida
    assert algoritmo_luhn("4539319503436467") == True
    assert algoritmo_luhn("6011514433546201") == True
    
    # Tarjeta inválida
    assert algoritmo_luhn("1234567812345678") == False


def test_usuario_creacion_valida():
    
    usuario = Usuario(nombre="Paco", username="magic_paco", password="123.", tarjeta="4539319503436467")
    assert usuario.nombre == "Paco"
    assert usuario.username == "magic_paco"
    assert usuario.password == "123."
    assert usuario.tarjeta == "4539319503436467"  

def test_usuario_tarjeta_invalida():
    with pytest.raises(error_algoritmo_luhn):
        Usuario(nombre="Paco", username="magic_paco", password="123.", tarjeta="1234567812345678")

def test_usuario_formato_tarjeta_invalido():
    with pytest.raises(error_de_formato):
        Usuario(nombre="Paco", username="magic_paco", password="123.", tarjeta="Tarjeta58")

def test_usuario_caracteres_insuficientes():
    # Caso donde el número de caracteres de la tarjeta es insuficiente
    with pytest.raises(error_numero_caracteres):
        Usuario(nombre="Paco", username="magic_paco", password="123.", tarjeta="3")
