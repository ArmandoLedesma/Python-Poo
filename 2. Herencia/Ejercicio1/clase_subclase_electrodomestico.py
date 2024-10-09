#Ejercicio 1: Clase Electrodomestico y Subclase Refrigerador 

#Definición de la clase principal o clase Padre "Electrodomestico"
class Electrodomestico:
    #Creación del método constructor 
    def __init__(self, marca, color, capacidad):
        #Definimos los atributos de la clase "Electrodomestico" usando la palabra reservada "self"
        self.marca = marca 
        self.color = color
        self.capicidad = capacidad
        #Agregamos un atributo adicional que será requerido por el usuario
        self.consumo_electrico = int(input("Ingrese el consumo en (kWh): "))
    
    #Creación del método Registrar_el_Electrodomestico() que muestre los detalles
    def Registrar_Electrodomestico(self):
        print(
            f"""
            -----------------------------
            Registro de Electrodomesticos
            ----------------------------- \n
            Marca: {self.marca}
            Color: {self.color}
            Capacidad: {self.capicidad}
            Consumo Electrico: {self.consumo_electrico}   
            -----------------------------         
            """
        )
    
#Creación de la Subclase "Refrigerador"
class Refrigerador(Electrodomestico):
    #Extracción del método constructor del padre "Electrodomestico"
    def __init__(self, marca, color, capacidad, tipo_refrigerador):
        super().__init__(marca, color, capacidad)
        #Definimos los atributos de la subclase "Refrigerador" usando la palabra reservada "self"
        self.tipo_refrigerador = tipo_refrigerador
        #Agregamos un atributo adicional de la subclase "Refrigerador()" que será requerido por el usuario
        self.temperatura = int(input("Ingrese la temperatura (°C): "))

       
    
    
    #Creación del método que nos ayudara ajustar la temperatura 
    def ajustar_temperatura(self):
        print(f"Tipo de refrigerador: {self.tipo_refrigerador}")
        
        if self.temperatura > 2 and self.temperatura <= 8:
            print(f"Temperatura del refrigerador {self.temperatura} °C, Considerada normal.")
        else:
            print(f"La temperatura debe ser regulada... ")

#Creación de los objetos 
refrigerador1 = Refrigerador("Mabe", "Gris", 200, "No Frost")

#Llamado de los métodos 
refrigerador1.Registrar_Electrodomestico()
refrigerador1.ajustar_temperatura()
        
    
    
    
        
        