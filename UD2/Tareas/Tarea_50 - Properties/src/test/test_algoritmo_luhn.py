import pytest
from Tarea_50.usuario import Usuario
from Tarea_50.errores import error_algoritmo_luhn

# Crear un usuario con tarjeta válida
def test_crear_usuario_tarjeta_valida():
    usuario = Usuario(nombre="Paco", username="magic_paco", password="123.", tarjeta="4539319503436467")
    assert usuario.nombre == "Paco"
    assert usuario.username == "magic_paco"
    assert usuario.password == "123."
    assert usuario.tarjeta == "4539319503436467"

# Test: Crear un usuario sin tarjeta
def test_crear_usuario_sin_tarjeta():
    usuario = Usuario(nombre="Maria", username="maria123", password="abc123")
    assert usuario.nombre == "Maria"
    assert usuario.username == "maria123"
    assert usuario.password == "abc123"
    assert usuario.tarjeta is None

# Crear un usuario con tarjeta inválida
def test_crear_usuario_tarjeta_invalida():
    with pytest.raises(error_algoritmo_luhn) as excinfo:
        Usuario(nombre="Juan", username="juanito", password="password", tarjeta="1234567890123456")
    assert "1234567890123456" in str(excinfo.value)

# Cambiar a un numero de tarjeta válido
def test_cambiar_tarjeta_valida():
    usuario = Usuario(nombre="Carlos", username="carlos123", password="pass123", tarjeta="6011 5144 3354 6201")
    usuario.tarjeta = "4539 3195 0343 6467"  
    assert usuario.tarjeta == "4539 3195 0343 6467" # Acepta el nuevo numero, por lo que cambia

# Cambiar a un numero de tarjeta inválido
def test_cambiar_tarjeta_invalida():
    usuario = Usuario(nombre="Ana", username="ana456", password="123abc", tarjeta="4539319503436467")
    with pytest.raises(error_algoritmo_luhn) as excinfo:
        usuario.tarjeta = "1234567890123456"  
    assert usuario.tarjeta == "4539319503436467"  # El nuevo numero no es valido, por lo que no cambia
    assert "1234567890123456" in str(excinfo.value)

def test_cambiar_tarjeta_a_none():
    usuario = Usuario(nombre="Laura", username="laura789", password="pass456", tarjeta="4539319503436467")
    usuario.tarjeta = None  # Tarjeta eliminada
    assert usuario.tarjeta is None
