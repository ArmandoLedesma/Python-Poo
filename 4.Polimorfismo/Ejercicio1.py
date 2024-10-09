#Ejercicio 1: Clase "Aprendiz" con polimorfismo

#Creación de la clase principal o clase padre "Aprendiz"
class Aprendiz:
    #Creación del método constructor junto con cada instancia
    def __init__(self, nombres, apellidos, cedula, sexo):
        #Definición de los atributos previamente instanciados
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.sexo = sexo
        self.formacion = str(input("Programa de formación: ")) #Atributo adicional requerido por el usuario
        self.regional = str(input("Regional: ")) #Atributo requerido adicional por el usuario

    
    #Creación del método "mostrar_info()" que mostrará los detalles en pantalla
    def mostrar_info(self):
        print("--------------------------------")
        print("Hola, soy un aprendiz del SENA")
        print(f"--------------------------------\n")
        print(f"Nombre completo: {self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Sexo: {self.sexo}")
        print(f"Programa de formación: {self.formacion}")
        print(f"Regional: {self.regional}")


#Creación de la subclase o clase hija "Instructor"
class Instructor(Aprendiz): #Herencia
    #Extracción del método constructor perteneciente a la clase padre "Aprendiz"
    def __init__(self, nombres, apellidos, cedula, sexo, area):
        #Creación del supermetodo perteneciente a la clase hija "Instructor"
        super().__init__(nombres, apellidos, cedula, sexo)
        #Definición del atributo adicional previamente instanciado
        self.area = area
        
    #Creación del método "mostrar_info()" que mostrará los detalles en pantalla
    def mostrar_info(self):
        print("--------------------------------")
        print("Hola, soy un instructor del SENA")
        print(f"--------------------------------\n")
        print(f"Nombre completo: {self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Area de instrucción: {self.area}")
        
#Creación de la subclase o clase hija "Cordinador"
class Cordinador(Aprendiz):
    #Extracción del método constructor perteneciente a la clase padre "Aprendiz"
    def __init__(self, nombres, apellidos, cedula, sexo, departamento):
        #Creación del supermetodo perteneciente a la clase hija "Cordinador"
        super().__init__(nombres, apellidos, cedula, sexo)
        #Definición del atributo adicional previamente instanciado
        self.departamento = departamento 
        
        
    #Creación del método "mostrar_info()" que mostrará los detalles en pantalla
    def mostrar_info(self):
        print("--------------------------------")
        print("Hola, soy el cordinador del SENA")
        print(f"--------------------------------\n")
        print(f"Nombre completo: {self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Departamento: {self.departamento}")
        
#Función que muestra la información de cualquier tipo de objeto
def mostrar_informacion(persona):
    persona.mostrar_info()

#Creación de objetos
objeto_aprendiz = Aprendiz("Leonardo Andres", "Vega Barrios", 12345678, "M")
objeto_instructor = Instructor("Luisa Vanessa", "Mesa Sambrano", 123456789, "F", "Analisis y Desarrollo de Software")
objeto_cordinador = Cordinador("Miguel Antonio", "Bernal Ruiz", 92378945, "M", "Academico")

#Llamado a los métodos
mostrar_informacion(objeto_aprendiz)
mostrar_informacion(objeto_instructor)
mostrar_informacion(objeto_cordinador)
    
    
    