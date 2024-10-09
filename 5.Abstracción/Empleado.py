from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual
        
    def calcular_salario(self):
        return self.salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, tarifa_por_hora, horas_trabajadas):
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = horas_trabajadas
    
    def calcular_salario(self):
        return self.tarifa_por_hora * self.horas_trabajadas


empleado1 = EmpleadoTiempoCompleto(3000)  
print(f'Salario del empleado a tiempo completo: {empleado1.calcular_salario()}')

empleado2 = EmpleadoPorHoras(20, 120) 
print(f'Salario del empleado por horas: {empleado2.calcular_salario()}')
