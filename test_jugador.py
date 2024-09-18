import pytest
from jugador import Jugador

def test_prueba():
    assert True

def test_constructor():
    jugador = Jugador("alex")
    assert jugador.fichas == 5

def test_str():
    jugador = Jugador("alex")
    msj = str(jugador)
    assert "alex" in msj
    assert "fichas" in msj
    assert "6" in msj

def test_darFicha():
    jugador = Jugador("alex")
    jugador.darFicha(3)
    assert jugador.fichas == 8

    jugador = Jugador("alex")
    jugador.darFicha(5)
    assert jugador.fichas == 10

def test_sacarFicha():
    jugador = Jugador("alex")
    jugador.sacarFicha(3)
    assert jugador.fichas == 2

    jugador = Jugador("alex")
    jugador.sacarFicha(5)
    assert jugador.fichas == 0

def test_sacarFicha_error():
    jugador = Jugador("alex")
    with pytest.raises(ValueError):
        jugador.sacarFicha(6)

def test_tieneFicha():
    jugador = Jugador("alex")
    assert jugador.tieneFicha()
    jugador.sacarFicha(4)
    assert jugador.tieneFicha(1)
    assert not jugador.tieneFicha(5)

def test_sinFichas():
    jugador = Jugador("alex")
    assert not jugador.sinFichas()
    jugador.sacarFicha(5)
    assert jugador.sinFichas()