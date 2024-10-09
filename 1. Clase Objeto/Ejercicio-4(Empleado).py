class Empleado:
    def __init__(self, nombre, puesto, departamento, salario, fecha_contratacion):
        self.nombre = nombre
        self.puesto = puesto 
        self.departamento = departamento
        self.salario = salario 
        self.fecha_contratacion = fecha_contratacion

    #Métodos para mostrar detalles de los objetos
    def mostrar_detalles(self):
        print(
            f"""
            Detalles del empleado
            --------------------------
            Nombre: {self.nombre} 
            Puesto: {self.departamento}
            Salario: {self.salario}
            Fecha de Contratación: {self.fecha_contratacion}
            --------------------------
            """
        )
    
    

Empleado1 = Empleado("Pedro", "Gerente", "Ventas", "2.000.000", "13/05/2020")
Empleado2 = Empleado("Antonio", "Operario Maquinas", "Planta Producción", "3.000.000", "20/09/2022")
Empleado3 = Empleado("Miguel", "Entrenador", "Gimnasio", "1.800.000", "03/02/2019")

Empleado1.mostrar_detalles()
Empleado2.mostrar_detalles()
Empleado3.mostrar_detalles()




