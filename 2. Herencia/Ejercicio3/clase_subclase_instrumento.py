#Ejercicio 3: Clase instrumento y Subclase Guitarra

#Definición de la clase principal o clase Padre "Instrumento"
class Instrumento:
    #Creación del método constructor con sus instancias
    def __init__(self, tipo_instrumento, marca, material_fabricacion):
        #Definimos los atributos instanciados usando la palabra "Self"
        self.tipo_instrumento = tipo_instrumento
        self.marca = marca 
        self.material_fabricacion = material_fabricacion
        #Definición de un atributo adicional requerido por el usuario para ingresar el precio
        self.precio = float(input("Ingrese el precio del instrumento: "))
        
    #Creación del método Registrar_Detalles para mostrar en pantalla
    def Registrar_Detalles(self):
        print(
            f"""
            --------------------
            Detalles Registrados
            -------------------- \n
            Tipo de Instrumento: {self.tipo_instrumento}
            Marca: {self.marca}
            Material de Fabricación: {self.material_fabricacion}
            Precio: {self.precio}
            --------------------
            """
        )
        
#Definición de la subclase o clase hija "Guitarra"
class Guitarra(Instrumento):
    #Extracción del método constructor con sus instancias
    def __init__(self, tipo_instrumento, marca, material_fabricacion, numero_cuerdas):
        super().__init__(tipo_instrumento, marca, material_fabricacion)
        #Definición del atributo adicional propio de la clase hija para el número de cuerdas 
        self.numero_cuerdas = numero_cuerdas
        #Definición del atributo adicional propio de la clase hija para los acordes básicos
        self.acordes_basicos = str(input("¿Cuantos acordes conoce?: ")).split(',')
    
    #Creación del método para simular tocar la guitarra
    def Tocar_Guitarra(self):
        print("¡Empecemos a tocar!")
        for acorde in self.acordes_basicos:
            print(f"Tocando acorde de: {acorde}")

#Creación del objeto
guitarra1 = Guitarra("Guitarra", "Española", "Cedro", 6)

#Llamado de los métodos para la clase hija "Guitarra"
guitarra1.Registrar_Detalles()
guitarra1.Tocar_Guitarra()