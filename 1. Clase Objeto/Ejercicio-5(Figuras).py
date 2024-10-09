class Figura:
    def __init__(self, nombre, puntos, lineas, lados, clasificacion):
        self.nombre = nombre
        self.puntos = puntos 
        self.lineas = lineas
        self.lados = lados 
        self.clasificacion = clasificacion

    #Métodos para mostrar detalles de los objetos
    def mostrar_detalles(self):
        print(
            f"""
            Detalles de las figuras 
            --------------------------
            Nombre: {self.nombre} 
            Puntos: {self.puntos}
            Lineas: {self.lineas}
            Lados: {self.lados}
            Clasificación: {self.clasificacion}
            --------------------------
            """
        )
    
    def calcular_perimetro(self):
        l1 = float(input("Ingrese el primer lado: "))
        l2 = float(input("Ingrese el segundo lado: "))
        l3 = float(input("Ingrese el tercer lado: "))
        l4 = float(input("Ingrese el cuarto lado: "))

        perimetro = l1 + l2 + l3 + l4

        print(f"El perimetro del {self.nombre} es: {perimetro}")        
    
    

Figura1 = Figura("Cuadrado", "4 Puntos", "4 lineas", "4 Lados", "Polígono")
Figura2 = Figura("Rectangulo", "4 puntos", "4 lineas", "4 Lados", "Polígono")
Figura3 = Figura("Rombo", "4 Puntos", "4 Lineas", "4 Lados", "Rombo")

Figura1.mostrar_detalles()
Figura2.mostrar_detalles()
Figura3.mostrar_detalles()

Figura1.calcular_perimetro()