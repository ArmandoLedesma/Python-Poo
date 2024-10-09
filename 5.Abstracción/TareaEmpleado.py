from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(TareaEmpleado):
    def __init__(self, especialidad):
        self.especialidad = especialidad
        
    def realizar_tarea(self):
        return f'El ingeniero de especialidad {self.especialidad} está diseñando un nuevo proyecto.'

class Doctor(TareaEmpleado):
    def __init__(self, especialidad):
        self.especialidad = especialidad
    
    def realizar_tarea(self):
        return f'El doctor de especialidad {self.especialidad} está atendiendo a un paciente.'


ingeniero = Ingeniero("Civil")
print(ingeniero.realizar_tarea())

doctor = Doctor("Pediatría")
print(doctor.realizar_tarea())
