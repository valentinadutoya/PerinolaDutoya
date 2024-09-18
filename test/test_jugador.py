import pytest
from jugador import Jugador

def test_constructor():
    a = Jugador()
    assert(a.nombre == "jugador-x")
    assert(a.fichas == 5)

def test_repr():
    a = Jugador()
    msj = a.__repr__()
    assert (f"{a.nombre}, {a.fichas} ficha/s" in msj)

def test_darFicha():
    a = Jugador()
    a.darFicha(8)
    assert(a.fichas == 13)

    a = Jugador()
    a.darFicha(2)
    assert(a.fichas == 7)

    a = Jugador()
    a.darFicha(2)
    a.darFicha(2)
    assert(a.fichas == 9)

def test_sacarFicha_sin_argumentos():
    a = Jugador()
    a.fichas = 5
    a.sacarFicha()
    assert(a.fichas == 4)

def test_darFicha_sin_argumentos():
    a = Jugador()
    a.fichas = 5
    a.darFicha()
    assert(a.fichas == 6)