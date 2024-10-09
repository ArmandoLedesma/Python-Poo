#Ejercicio 4: Clase "Instrumentos" con polimorfismo

#Creación de la clase principal o clase padre "Instrumentos"
class Instrumentos:
    #Creación del método constructor junto con cada instancia
    def __init__(self, nombre, tipo, marca, material):
        #Definición de los atributos previamente instanciados
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.material = material

#Creación de la subclase o clase hija "Guitarra"
class Guitarra(Instrumentos): #Herencia
    #Extracción del método constructor pertenciente a la clase padre "Instrumentos"
    def __init__(self, nombre, tipo, marca, material):
        #Creación del supermetodo perteneciente a la clase hija "Guitarra"
        super().__init__(nombre, tipo, marca, material)
        #Definición del atributo adicional requerido por el usuario
        self.tocar = str(input("Toca una nota músical: ")).upper()

    #Creación del método "Tocar()" que simulará el toque del instrumento 
    def Tocar(self): 
        print(f"En la {self.nombre} estas tocando la nota {self.tocar}!") 

#Creación de la subclase o clase hija "Piano"
class Piano(Instrumentos): #Herencia 
    #Extracción del método constructor pertenciente a la clase padre "Instrumentos"
    def __init__(self, nombre, tipo, marca, material):
        #Creación del supermetodo perteneciente a la clase hija "Piano"
        super().__init__(nombre, tipo, marca, material)
        #Definición del atributo adicional requerido por el usuario
        self.tocar = str(input("Toca una nota músical: ")).upper()
       
    
    #Creación del método "Tocar()" que debera usado para cada clase 
    def Tocar(self): 
        print(f"En el {self.nombre} estas tocando la nota {self.tocar}!") 

#Creación de la subclase o clase hija "Trompeta"
class Trompeta(Instrumentos): #Herencia 
    #Extracción del método constructor perteneciente a la clase padre "Instrumentos"
    def __init__(self, nombre, tipo, marca, material):
       #Creación del supermetodo perteneciente a la clase hija "Tocar"
       super().__init__(nombre, tipo, marca, material)
       #Definición del atributo adicional requerido por el usuario
       self.tocar = str(input("Toca una nota músical: ")).upper()
    
    #Creación del método "Tocar()" que debera usado para cada clase 
    def Tocar(self): 
        print(f"En el {self.nombre} estas tocando la nota {self.tocar}!")  


#Función que muestra el sonido de cualquier tipo de Instrumento
def tocar_instrumento(tocar):
    tocar.Tocar()

#Creación de los objetos 
objeto_guitarra = Guitarra("Guitarra", "Acustica", "Española", "Cedro")
objeto_piano = Piano("Piano", "Cuerdas", "Yamaha", "Cedro")
objeto_trompeta = Trompeta("Trompeta", "Viento", "Found", "Aluminio")

#Llamado a los métodos
tocar_instrumento(objeto_guitarra)
tocar_instrumento(objeto_piano)
tocar_instrumento(objeto_trompeta)
    