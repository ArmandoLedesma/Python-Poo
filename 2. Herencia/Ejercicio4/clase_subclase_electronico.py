class Electronico:
    def __init__(self, marca, modelo, procesador):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = int(input("Ingrese la cantidad de RAM en GB: "))

    def mostrar_detalles(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")

class Laptop(Electronico):
    def __init__(self, marca, modelo, procesador, disco_duro, bateria):
        super().__init__(marca, modelo, procesador)
        self.disco_duro = disco_duro
        self.bateria = bateria

    def encender(self):
        print("Encendiendo laptop...")
        print("Detalles de la laptop:")
        self.mostrar_detalles()
        print(f"Disco duro: {self.disco_duro}")
        print(f"Duración de la batería: {self.bateria} horas")

# Crear una instancia de la clase Laptop
mi_laptop = Laptop("Dell", "XPS 13", "Intel Core i7", "SSD 512GB", 10)

# Encender la laptop
mi_laptop.encender()