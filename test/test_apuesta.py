import pytest
from Apuestas import Apuestas

def setUp(self):
    self.apuestas = Apuestas("valen", 15)

def test_repr(self):
        self.assertEqual(repr(self.apuestas), "valen, 15 fichas")

def test_dar_ficha(self):
        self.apuestas.darFicha(5)
        self.assertEqual(self.apuestas.fichas, 20)

def test_poner_ficha(self):
        self.apuestas.ponerFicha(10)
        self.assertEqual(self.apuestas.fichas, 5) 
        
      
        self.apuestas.ponerFicha(5)
        self.assertEqual(self.apuestas.fichas, 0)

def test_poner_ficha_insuficiente(self):
        with self.assertRaises(ValueError):
            self.apuestas.ponerFicha(20)  

def test_tiene_ficha(self):
        self.assertTrue(self.apuestas.tieneFicha(5))
        self.assertFalse(self.apuestas.tieneFicha(20))

def test_sin_fichas(self):
        self.assertFalse(self.apuestas.sinFichas())
        self.apuestas.ponerFicha(15)  
        self.assertTrue(self.apuestas.sinFichas())