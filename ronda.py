class Jugador:
    def __init__(self, nombre, fichas=5):
        self.nombre = nombre
        self.fichas = fichas

    def __repr__(self):
        return f"{self.nombre}, {self.fichas} fichas"

    def sinFichas(self):
        return self.fichas == 0

class Ronda:
    def __init__(self):
        self.jugadores = []  

    def __str__(self):
        return "\n".join(str(jugador) for jugador in self.jugadores)

    def agregarJugador(self, jugador):
        if jugador.sinFichas():
            raise ValueError("El jugador no tiene fichas y no puede ser agregado.")
        self.jugadores.append(jugador) 

    def sacarJugadoresSinFichas(self):
        self.jugadores = [jugador for jugador in self.jugadores if not jugador.sinFichas()] 

    def jugadorEnTurno(self):
        return self.jugadores[0] if self.jugadores else None  

    def pasarTurno(self):
        if self.jugadores:  
            jugador = self.jugadores.pop(0)  
            self.jugadores.append(jugador)  

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1 

    def noQuedanJugadores(self):
        return len(self.jugadores) == 0 