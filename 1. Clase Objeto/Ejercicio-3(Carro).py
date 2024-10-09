class Carro: 
    def __init__(self, marca, modelo, peso, tamano, color):
        self.marca = marca
        self.modelo = modelo
        self.peso = peso
        self.tamano = tamano 
        self.color = color
    
        
    #Métodos para mostrar detalles de los objetos
    def mostrar_detalles(self):
        print(
            f"""
            Detalles de los autos 
            --------------------------
            Marca: {self.marca} 
            Modelo: {self.modelo}
            Peso: {self.peso}
            Tamaño: {self.tamano}
            Color: {self.color}
            --------------------------
            """
        )
    
    def movimiento(self):
        velocidades = [10,20,30,40,50,60,70,80,90,100]
        velocidad = int(input("Ingrese la velocidad a la que va el auto: "))
        
        if velocidad in velocidades:
            print(f"El auto {self.marca} está en marcha")
        else: 
            print(f"El auto {self.marca} no está en marcha")

Carro1 = Carro("Audi", "A4", "1500KG", "1,4M", "Rojo")
Carro2 = Carro("Toyota", "Carolla", "1500KG", "4,6M", "Plata")
Carro3 = Carro("Honda", "Civic", "1300KG", "4,7M", "Gris")

#Mostrar los detalles de los objetos creados (Animales)
Carro1.mostrar_detalles()
Carro2.mostrar_detalles()
Carro3.mostrar_detalles()

Carro1.movimiento()
       