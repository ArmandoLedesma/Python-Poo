#Ejercicio 3: Clase Libro

#Creamos la clase principal o clase padre "Libro"
class Libro:
    #Creamos el método constructor junto con cada instancia 
    def __init__(self, titulo, autor, isbn, editorial):
        #Definición de los atributos previamente instanciados
        self.__titulo = titulo #Atributo privado
        self.__autor = autor #Atributo privado
        self.__isbn = isbn #Atributo privado
        self.editorial = editorial #Atributo público 
        
    #Usamos el método GET para obtener los valores encapsulados del atributo "titulo"
    def obtener_titulo(self):
        return self.__titulo
    
    #Usamos el método GET para obtener los valores encapsulados del atributo "autor"
    def obtener_autor(self):
        return self.__autor
    
    #Usamos el método GET para obtener los valores encapsulados del atributo "isbn"
    def obtener_isbn(self):
        return self.__isbn
    
    #Usamos el método SET para modificar los valores encapsulados del atributo "titulo"
    def establecer_titulo(self, nuevo_nombre):
        self.__titulo = nuevo_nombre
        
    #Usamos el método SET para modificar los valores encapsulados del atributo "autor"
    def establecer_autor(self, nuevo_apellido):
        self.__autor = nuevo_apellido
        
    
    #Creación del método que nos permitirá ver los detalles de los objetos 
    def mostrar_detalles(self):
        print(f"------------------------")
        print(f"Detalles del Libro")
        print(f"------------------------")
        print(f"titulo: {self.__titulo}")
        print(f"autor: {self.__autor}")
        print(f"isbn: {self.__isbn}")
        print(f"editorial: {self.editorial}")

#Creación del objeto
libro = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "978-84-376-0494-7", "Sudamerica")  

libro.mostrar_detalles()

#Imprimir los atributos públicos y privados

#Salto de linea
print(f"\n")   

#Imprimir los atributos encapsulados modificando su acceso con SET Y GET
libro.establecer_titulo("El alquimista") #SET
print(f"titulo: {libro.obtener_titulo()}") 
libro.establecer_autor("Paulo Coelho") #SET
print(f"autor: {libro.obtener_autor()}") #GET
print(f"isbn: {libro.obtener_isbn()}") #GET
print(f"editorial: {libro.editorial}") #Atributo público
