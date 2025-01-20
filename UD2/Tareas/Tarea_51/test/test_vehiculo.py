import pytest
from src.vehiculo import Vehiculo
from src.exceptions import velocidad_negativa, disminuir_total_kms


def test_crear_vehiculo():
    vehiculo = Vehiculo(200, 100)
    assert vehiculo.max_vel == 200
    assert vehiculo.total_kms == 100
    assert vehiculo.mostrar_vehiculo() == "Velocidad máxima: 200, kilometraje: 100"


def test_velocidad_negativa():
    vehiculo = Vehiculo(200, 100)
    with pytest.raises(velocidad_negativa) as excinfo:
        vehiculo.max_vel = -50
    assert str(excinfo.value) == "La velocidad no puede tener un valor negativo. (-50)"


def test_disminuir_total_kms():
    vehiculo = Vehiculo(200, 100)
    with pytest.raises(disminuir_total_kms) as excinfo:
        vehiculo.total_kms = 50
    assert str(excinfo.value) == (
        "El kilometraje no puede decrecer. (Valor previo: 100 Intento de nuevo valor: 50)"
    )


def test_actualizar_max_vel_ok():
    vehiculo = Vehiculo(200, 100)
    vehiculo.max_vel = 150
    assert vehiculo.max_vel == 150


def test_actualizar_total_kms_ok():
    vehiculo = Vehiculo(200, 100)
    vehiculo.total_kms = 150
    assert vehiculo.total_kms == 150


