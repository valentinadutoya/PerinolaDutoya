class Jugador:
    def __init__(self, nombre="jugador-x", fichas=5):
        self.nombre = nombre
        self.fichas = fichas
    
    def __repr__(self):
        return f"{self.nombre}, {self.fichas} ficha/s"
    
    def darFicha(self, cuantas=1):
        self.fichas = self.fichas + cuantas

    def sacarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError ("No tiene suficientes fichas")
        else: 
            self.fichas = self.fichas - cuantas
    
    def tieneFicha(self, cuantas = 1):
        if self.fichas == cuantas:
            return True
        
    def sinFichas(self):
        if self.fichas == 0:
            return True