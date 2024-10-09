# Clase principal o clase padre "Profesional"
class Profesional:
    def __init__(self, nombre, especialidad, experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.experiencia = experiencia

# Clase "Medico"
class Medico(Profesional):
    def __init__(self, nombre, especialidad, experiencia):
        super().__init__(nombre, especialidad, experiencia)
    
    def trabajar(self):
        print(f"{self.nombre} es médico especializado en {self.especialidad} con {self.experiencia} años de experiencia.")

# Clase "Ingeniero"
class Ingeniero(Profesional):
    def __init__(self, nombre, especialidad, experiencia):
        super().__init__(nombre, especialidad, experiencia)
    
    def trabajar(self):
        print(f"{self.nombre} es ingeniero especializado en {self.especialidad} con {self.experiencia} años de experiencia.")

# Clase "Docente"
class Docente(Profesional):
    def __init__(self, nombre, especialidad, experiencia):
        super().__init__(nombre, especialidad, experiencia)
    
    def trabajar(self):
        print(f"{self.nombre} es docente especializado en {self.especialidad} con {self.experiencia} años de experiencia.")

# Función que muestra el trabajo de cualquier tipo de profesional
def trabajar_profesional(profesional):
    profesional.trabajar()

# Creación de los objetos 
objeto_medico = Medico("Dr. Pérez", "Cardiología", 10)
objeto_ingeniero = Ingeniero("Ing. López", "Civil", 5)
objeto_docente = Docente("Profa. García", "Matemáticas", 8)

# Llamado a los métodos
trabajar_profesional(objeto_medico)
trabajar_profesional(objeto_ingeniero)
trabajar_profesional(objeto_docente)
