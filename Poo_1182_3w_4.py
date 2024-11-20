class Persona():
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        print(self.nombre + " " + self.apellido)  

class Estudiante(Persona):
    def __init__(self, nom, ape, carrera):  
        super().__init__(nom, ape)  
        self.carrera = carrera

    def mostrar_carrera(self):
        print(self.carrera)  


estudiante = Estudiante("Gael", "Garcia", "Programacion")
estudiante.nombre_completo()  
estudiante.mostrar_carrera()  
