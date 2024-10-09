#Ejercicio 3: Clase "Animales" con polimorfismo

#Creación de la clase principal o clase padre "Animales"
class Animales:
    #Creación del método constructor junto con cada instancia
    def __init__(self, especie, nombre, edad, peso, altura):
        #Definición de los atributos previamente instanciados
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.sonido = str(input("Sonido del animal: ")) #Atributo adicional requerido por el usuario

    #Creación del método "Sonido()" que debera usado para cada clase 
    def Sonido(self): 
        print(f"{self.especie} hace el sonido {self.sonido}")

#Creación de la subclase o clase hija "Perro"
class Perro(Animales): #Herencia
    #Extracción del método constructor perteneciente a la clase padre "Animales"
    def __init__(self, especie, nombre, edad, peso, altura, color):
        #Creación del supermetodo perteneciente a la clase hija "Perro"
        super().__init__(especie, nombre, edad, peso, altura)
        #Definición del atributo adicional previamente instanciado
        self.color = color #Atributo adicional
        self.sonido = str(input("Sonido del Perro: ")) #Atributo adicional requerido por el usuario

    #Creación del método "Sonido()" que debera ser usado para cada clase 
    def Sonido(self): 
        print(f" El {self.especie} ladra {self.sonido}!")
    

#Creación de la subclase o clase hija "Gato"
class Gato(Animales): #Herencia 
    #Extracción del método constructor perteneciente a la clase padre "Animales"
    def __init__(self, especie, nombre, edad, peso, altura, color):
        #Creación del supermetodo perteneciente a la clase hija "Gato"
        super().__init__(especie, nombre, edad, peso, altura)
        #Definición del atributo adicional previamente instanciado
        self.color = color #Atributo adicional
        self.sonido = str(input("Sonido del Gato: ")) #Atributo adicional requerido por el usuario

    #Creación del método "Sonido()" que debera ser usado para cada clase 
    def Sonido(self): 
        print(f" El {self.especie} maulla {self.sonido}!") 

#Creación de la subclase o clase hija "Pajaro"
class Pajaro(Animales): #Herencia 
    #Extracción del método constructor perteneciente a la clase padre "Animales"
    def __init__(self, especie, nombre, edad, peso, altura, color):
        #Creación del supermetodo perteneciente a la clase hija "Pajaro"
        super().__init__(especie, nombre, edad, peso, altura)
        #Definición del atributo adicional previamente instanciado
        self.color = color #Atributo adicional
        self.sonido = str(input("Sonido del Pajaro: ")) #Atributo adicional requerido por el usuario
        
    
    #Creación del método "Sonido()" que debera usado para cada clase 
    def Sonido(self): 
        print(f"El {self.especie} canta {self.sonido}!") 


#Función que muestra el sonido de cualquier tipo de Animal
def generar_sonido(sonido):
    sonido.Sonido()

#Creación de los objetos 
objeto_animal = Animales("Vaca", "Lola", 8, "1.200KG", "1,80CM")
objeto_perro = Perro("Doberman", "Saul", 3, "60KG", "80CM", "Negro")
objeto_gato = Gato("Gato", "Michin", 2, "10KG", "20CM", "Naranja")
objeto_pajaro = Pajaro("Tucan", "Miguelito", 3, "2KG", "1,5CM", "Multicolor")

#Llamado a los métodos
generar_sonido(objeto_perro)
generar_sonido(objeto_gato)
generar_sonido(objeto_pajaro)
    
    