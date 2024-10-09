from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass 

class Cuadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self):
        return self.lado ** 2

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
cuadrado = Cuadrado(5)
print(f'Área del cuadrado: {cuadrado.calcular_area()}')

circulo = Circulo(3)
print(f'Área del círculo: {circulo.calcular_area()}')