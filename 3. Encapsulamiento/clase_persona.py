#Ejercicio 1: Clase Persona 

#Creamos la clase principal o clase padre "Personas"
class Personas:
    #Creamos el método constructor junto con cada instancia 
    def __init__(self, nombres, apellidos, identidad, fecha_nacimiento, sexo):
        #Definición de los atributos previamente instanciados
        self.__nombres = nombres #Atributo privado
        self.__apellidos = apellidos #Atributo privado
        self.__identidad = identidad #Atributo privado
        self.fecha_nacimiento = fecha_nacimiento #Atributo público 
        self.sexo = sexo #Atributo público
        
    #Usamos el método GET para obtener los valores encapsulados del atributo "nombres"
    def obtener_nombres(self):
        return self.__nombres
    
    #Usamos el método GET para obtener los valores encapsulados del atributo "apellidos"
    def obtener_apellidos(self):
        return self.__apellidos
    
    #Usamos el método GET para obtener los valores encapsulados del atributo "identidad"
    def obtener_identidad(self):
        return self.__identidad
    
    #Usamos el método SET para modificar los valores encapsulados del atributo "nombres"
    def establecer_nombres(self, nuevo_nombre):
        self.__nombres = nuevo_nombre
        
    #Usamos el método SET para modificar los valores encapsulados del atributo "apellidos"
    def establecer_apellidos(self, nuevo_apellido):
        self.__apellidos = nuevo_apellido
        
    
    #Creación del método que nos permitirá ver los detalles de los objetos 
    def mostrar_detalles(self):
        print(f"-------------------------")
        print(f"Detalles de Persona")
        print(f"-------------------------")
        print(f"Nombres: {self.__nombres}")
        print(f"Apellidos: {self.__apellidos}")
        print(f"Identidad: {self.__identidad}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Sexo: {self.sexo}")
        print(f"-------------------------")

#Creación del objeto
persona = Personas("Jorge", "Rojas", 92540101, "14/09/2000", "M")  

persona.mostrar_detalles()

#Imprimir los atributos públicos y privados

#Salto de linea
print(f"\n")   

#Imprimir los atributos encapsulados modificando su acceso con SET Y GET
persona.establecer_nombres("Jader") #SET
print(f"Nombres: {persona.obtener_nombres()}") 
persona.establecer_apellidos("Perez") #SET
print(f"Apellidos: {persona.obtener_apellidos()}") #GET
print(f"Identidad: {persona.obtener_identidad()}") #GET
print(f"Fecha de Nacimiento: {persona.fecha_nacimiento}") #Atributo público
print(f"Sexo: {persona.sexo}") #Atributo público

        
        
        
        