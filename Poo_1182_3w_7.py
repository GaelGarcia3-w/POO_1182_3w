class Universidad():
    def __init__(self, nombre):
        self.Nombre = nombre

class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, universidad, nombre, edad):
        
        Universidad.__init__(self, universidad)
        
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")


persona = Estudiante("U.N.A.M", "Gael", 18)
persona.carrera("Administracion de empresas")
persona.datos()
