#Ejercicio 2: Clase Dispositivo y Subclase Smartphone

#Definimos la clase principal o clase Padre "Dispositivo"
class Dispositivo:
    #Creación del método constructor con las instancias 
    def __init__(self, marca, modelo, ano_fabricacion): #Definición de instancias 
        #Definición de los atributos usando la palabra "Self"
        self.marca = marca 
        self.modelo = modelo
        self.ano_fabricacion = ano_fabricacion
        #Atributo adicional capacidad_bateria que será requerida por el usuario
        self.capacidad_bateria = int(input("Ingrese la capacidad de la bateria (mAh): "))
    
    #Creación del método de Registro y Detalles de los dispositivos 
    def Registro_Detalles(self):
        print(
            f"""
            ------------------------
            Dispositivos Registrados
            ------------------------ \n
            Marca: {self.marca}
            Modelo: {self.modelo}
            Año de Fabricación: {self.ano_fabricacion}
            Capacidad de Bateria: {self.capacidad_bateria}
            ------------------------
            """
        )

#Creación de la subclase o clase hija Smartphone 
class Smartphone(Dispositivo):
    #Extracción del método constructor principal con sus instancias
    def __init__(self, marca, modelo, ano_fabricacion, sistema_operativo):
        super().__init__(marca, modelo, ano_fabricacion)
        #Definición del atributo adicional propio de la clase hija
        self.sistema_operativo = sistema_operativo
        #Definición del atributo adicional que debe ser requerido por el usuario
        self.tipo_conectividad = (input("Ingrese el tipo de conectividad (4G o 5G): ")).upper()

    #Creación del método para encender el Smartphone
    def encender(self):
        print(f"Conectividad del Smartphone {self.tipo_conectividad}")
        self.bateria = int(input("Ingrese el porcentaje de la bateria: "))
        if self.bateria > 0: 
            print(f"El dispotivo se puede encender...")
        else: 
            print(f"El dispositivo no puede encender...")

#Creación de los objetos
smartphone1 = Smartphone("Iphone", 11, 2019, 3110)

#Llamado de los métodos de la subclase Smartphone
smartphone1.Registro_Detalles()
smartphone1.encender()
    