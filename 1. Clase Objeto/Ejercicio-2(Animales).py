#Defino la clase Animal
class Animal:
    def __init__(self, animal, color, tamano, especie, habitad, edad_promedio):
        self.animal = animal
        self.color = color 
        self.tamano = tamano 
        self.especie = especie 
        self.habitad = habitad
        self.edad_promedio = edad_promedio
        
    #Métodos para mostrar detalles de los objetos
    def mostrar_detalles(self):
        print(
            f"""
            Caracteristicas del Animal 
            --------------------------
            animal: {self.animal} 
            Color: {self.color}
            Tamaño: {self.tamano}
            Especie: {self.especie}
            Habitad: {self.habitad}
            Edad Promedio: {self.edad_promedio}
            --------------------------
            """
        )
    
    def horario_comida(self):
        self.hora = float(input("Ingrese la hora: "))
        
        if self.hora <= 7: 
            print(f"¡Es hora del desayuno! El {self.animal} tiene hambre")
        elif self.hora >= 12:
            print(f"¡Es hora del almuerzo! El {self.animal} tiene hambre")
        else: 
            print(f"¡Es hora de la cena! El {self.animal} tiene hambre")

            
        
#Creación de los objetos
Animal1 = Animal("Gato", "Gris", "Pequeño", "Felino", "Domestico", "12-18 años")

Animal2 = Animal("Perro", "Blanco", "Mediano", "Canino", "Domestico", "10-15 años")

Animal3 = Animal("Loro Australiano", "Verde", "Pequeño", "Ave", "Domestico", "60 años")


#Mostrar los detalles de los objetos creados (Animales)
Animal1.mostrar_detalles()
Animal2.mostrar_detalles()
Animal3.mostrar_detalles()

Animal1.horario_comida()
Animal2.horario_comida()
Animal3.horario_comida()


        