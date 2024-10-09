class Reloj:
    def __init__(self, marca, tipo, material):
        self.marca = marca
        self.tipo = tipo
        self.material = material
        self.precio = float(input("Ingrese el precio del reloj: "))

    def registrar_detalles(self):
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Material: {self.material}")
        print(f"Precio: ${self.precio}")

class RelojInteligente(Reloj):
    def __init__(self, marca, tipo, material, pantalla, sistema_operativo):
        super().__init__(marca, tipo, material)
        self.pantalla = pantalla
        self.sistema_operativo = sistema_operativo

    def encender(self):
        print("Encendiendo reloj inteligente...")
        print("Detalles del reloj:")
        self.registrar_detalles()
        print(f"Pantalla: {self.pantalla}")
        print(f"Sistema operativo: {self.sistema_operativo}")


mi_reloj = RelojInteligente("Apple", "Deportivo", "Aluminio", "OLED", "watchOS")


mi_reloj.encender()