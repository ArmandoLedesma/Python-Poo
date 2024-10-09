#Definir la clase
class Celular:
    #Metodo constructor
    def __init__(self, marca, modelo, almacenamiento, ram, camara):
        #Definición de atributos de instancia para la clase
        self.marca = marca 
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.camara = camara
        
    #Métodos para mostrar detalles del objeto 
    def mostrar_detalles(self):
        print(
            f"""
            Información del Celular 
            --------------------------
            Marca: {self.marca} 
            Módelo: {self.modelo}
            Almacenamiento: {self.almacenamiento}
            Ram: {self.ram}
            Camara: {self.camara}
            --------------------------
            """
        )
    
    #Método para encender el celular 
    def encender(self):
        self.energia = int(input("Ingrese el valor de la carga: "))
        if self.energia > 0:
            print(f"El celular {self.modelo} se puede encender")
        else:
            print(f"El celular {self.modelo} no puede encender")
        
#Creación de objetos a partir de instaciar la clase Celular:
celular1 = Celular("Xiaomi", "Redmi Note 13", "256GB", "8GB", "108MPX")

celular2 = Celular("Apple", "Iphone 8 Plus", "256GB", "3GB", "12MPX")

celular3 = Celular("Apple", "Iphone 12 Pro", "256GB", "6GB", "12MPX")

#Mostrar los detalles de cada objeto
celular1.mostrar_detalles()
celular2.mostrar_detalles()
celular3.mostrar_detalles()

celular1.encender()
celular2.encender()
celular3.encender()
