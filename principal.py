from perinola import Perinola
from Apuestas import Apuestas
from jugador import Jugador

p = Perinola()
p.tirar()
print(p.cara_visible)



a = Apuestas()
a.ponerFichas(5)
print(a)

jugador = Jugador("valentina", 15)
print(jugador) 