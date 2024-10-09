#Ejercicio 2: Clase producto 

#Creamos la clase principal o clase padre "Producto"
class Producto:
    #Creamos el método constructor junto con cada instancia
    def __init__(self, nombre, precio, cantidad, categoria): #Los atributos "nombre" y "precio" serán "privados"
        #Definición de los atributos instanciados previamente
        self.__nombre = nombre #Privado
        self.__precio = precio #Privado
        self.cantidad = cantidad
        self.categoria = categoria 
        
    #Uso del método GET para obtener el nombre
    def obtener_nombre(self):
        return self.__nombre
    
    #Uso del método GET para obtener el precio
    def obtener_precio(self):
        return self.__precio
    
    #Uso del método SET para modificar los valores del atributo nombre
    def modificar_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    #Uso del método SET para modificar los valores del atributo precio
    def modificar_precio(self, nuevo_precio):
        self.__precio = nuevo_precio
    
    #Creación del método que permitirá mostrar los atributos de cada objeto creado por pantalla 
    def mostrar_detalles(self):
        print(f"-----------------------")
        print(f"Detalles del Producto")
        print(f"-----------------------")
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoría: {self.categoria}")
        print(f"-----------------------")
        
#Creación de los objetos
producto = Producto("Shampo de Coco", 2500, 15, "Aseo personal")

#Llamado al método mostrar_detalles()
producto.mostrar_detalles()

#Salto de linea 
print(f"\n")

#Imprimir los atributos encapsulados modificando su acceso con SET y GET
producto.modificar_nombre("Shampo de Avena") #Método SET
print(f"Nombre: {producto.obtener_nombre()}") #Imprimir la modificación del nombre del producto
producto.modificar_precio(1200) #Método SET
print(f"Precio: {producto.obtener_precio()}") #Imprimir la módificación del precio del producto
print(f"Nombre: {producto.obtener_nombre()}") #Imprimir el método GET
print(f"Precio: {producto.obtener_precio()}") #Imprimir el método GET
print(f"Cantidad: {producto.cantidad}")
print(f"Categoría: {producto.categoria}")