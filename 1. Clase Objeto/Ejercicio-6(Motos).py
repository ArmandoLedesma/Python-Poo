class Moto:
    def __init__(self, marca, modelo, motor, chasis, ruedas, suspension):
        self.marca = marca
        self.modelo = modelo 
        self.motor = motor
        self.chasis = chasis 
        self.ruedas = ruedas
        self.suspension = suspension

    #Métodos para mostrar detalles de los objetos
    def mostrar_detalles(self):
        print(
            f"""
            Detalles de la Moto
            --------------------------
            Marca: {self.marca} 
            Modelo: {self.modelo}
            Motor: {self.motor}
            Chasis: {self.chasis}
            Ruedas: {self.ruedas}
            Suspensión: {self.suspension}
            --------------------------
            """
        )
    
    def movimiento(self):
        velocidades = [10,20,30,40,50,60,70,80,90,100]
        velocidad = int(input("Ingrese la velocidad a la que va la moto: "))
        
        if velocidad in velocidades:
            print(f"La moto {self.marca} está en marcha")
        else: 
            print(f"La moto {self.marca} no está en marcha")
    
    

Moto1 = Moto("Suzuki Dr 650", "2017", "4 Tiempos", "Acero", "2 Ruedas", "Delantera y Trasera")
Moto2 = Moto("Yamaha Yz 250", "2024", "2 Tiempos", "Aluminio", "2 Ruedas", "Delantera y Trasera")
Moto3 = Moto("Kawasaki Klx 150", "2020", "4 Tiempos", "Aluminio", "2 Ruedas", "Delantera y Trasera")

Moto1.mostrar_detalles()
Moto2.mostrar_detalles()
Moto3.mostrar_detalles()

Moto1.movimiento()