#Ejercicio 2: Clase "Vehiculo" con polimorfismo

#Creación de la clase principal o clase padre "Vehiculo"
class Vehiculo:
    #Creación del método constructor junto con cada instancia
    def __init__(self, marca, modelo, ano, color, precio):
        #Definición de los atributos previamente instanciados 
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano
        self.color = color 
        self.precio = precio
    
    #Creación del método "Descripcion()" que me mostrará los detalles de cada tipo de vehiculos
    def Descripcion(self):
        print("------------------------")
        print("Descripción del Vehiculo")
        print(f"------------------------\n")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.ano}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")
        
#Creación de la subclase o clase hija "Carro" 
class Carro(Vehiculo): #Herencia
    #Extracción del método constructor perteneciente a la clase hija "Vehiculo"
    def __init__(self, marca, modelo, ano, color, precio, matricula):
        #Creación del supermetodo perteneciente a la clase hija "Carro"
        super().__init__(marca, modelo, ano, color, precio)
        #Definición del atributo adicional previamente instanciado
        self.matricula = matricula
    
    #Creación del método "Descripcion()" que me mostrará los detalles de cada tipo de vehiculos
    def Descripcion(self):
        print("------------------------")
        print("Descripción del Carro")
        print(f"------------------------\n")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.ano}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")
        print(f"Matricula: {self.matricula}")

#Creación de la subclase o clase hija "Moto"
class Moto(Vehiculo): #Herencia
    #Extracción del método constructor perteneciente a la clase padre "Vehiculo"
    def __init__(self, marca, modelo, ano, color, precio, cilindrada):
        #Creación del supermetodo perteneciente a la clase hija "Moto"
        super().__init__(marca, modelo, ano, color, precio)
        #Definición del atributo adicional previamente instanciado
        self.cilindrada = cilindrada
    
    #Creación del método "Descripcion()" que me mostrará los detalles de cada tipo de vehiculos
    def Descripcion(self):
        print("------------------------")
        print("Descripción de la Moto")
        print(f"------------------------\n")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.ano}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")
        print(f"Cilindrada: {self.cilindrada}")

#Creación de la subclase o clase hija "Bicicleta"
class Bicicleta(Vehiculo): #Herencia
    #Extracción del método constructor perteneciente a la clase padre "Vehiculo"
    def __init__(self, marca, modelo, ano, color, precio, tipo):
        #Creación del supermetodo perteneciente a la clase hija "Bicicleta"
        super().__init__(marca, modelo, ano, color, precio)
        #Definición del atributo adicional previamente instanciado
        self.tipo = tipo

    #Creación del método "Descripcion()" que me mostrará los detalles de cada tipo de vehiculos
    def Descripcion(self):
        print("------------------------")
        print("Descripción de la Bicicleta")
        print(f"------------------------\n")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.ano}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")
        print(f"Tipo: {self.tipo}")
        
#Función que muestra la información de cualquier tipo de Vehiculo
def mostrar_descripcion(vehiculo):
    vehiculo.Descripcion()

#Creación de los objetos 
objeto_vehiculo = Vehiculo("Ford", "Corolla", 2022, "Gris", 3000000000)
objeto_carro = Carro("Toyota", "Corolla Cross", 2020, "Azul", 250000000, "ABC-1234")
objeto_moto = Moto("Harley-Davidson", "Sportster", 2019, "Rojo", 7000000, "250cc")
objeto_bicicleta = Bicicleta("Trek", "Domane", 2018, "Plateada", 4000000, "Híbrida")

#Llamado a los métodos
mostrar_descripcion(objeto_vehiculo)
mostrar_descripcion(objeto_carro)
mostrar_descripcion(objeto_moto)
mostrar_descripcion(objeto_bicicleta)
