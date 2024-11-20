# POO_1182_3w
Edgar Gael Garcia Camacho 3-W
# #1
class Estudiante():

  def __init__(self, nombre, nota):
  
  self.nombre = nombre
  
  self.nota = nota
  
def imprimir(self):

  print(f"Nombre: {self.nombre} \nNota: {self.nota}")
  
  def resultados(self):
  
  if self.nota >= 7:
  
  print("Has APROBADO!")
  
  else:
  
  print("Has REPROBADO!")

#Creando los objetos Estudiante

estudiante1 = Estudiante("Noe", 5)

estudiante1.imprimir()

estudiante1.resultados()

estudiante2 = Estudiante("Gael", 10)

estudiante2.imprimir()

estudiante2.resultados()

 ![image](https://github.com/user-attachments/assets/6087fb7a-3141-446e-b8d4-737e4d9dcaf2) ![image](https://github.com/user-attachments/assets/00d4bf47-ec5c-4d95-a55f-de66b0009eb7) 
 ![image](https://github.com/user-attachments/assets/cab39ac6-ee44-4b9a-a970-df2c9a67df05)

# #2

class Persona:

  def __init__(self, n, e):
  
  self.nombre = n
  
  self.edad = e

  
  def cumpleaños(self):
  
  self.edad += 1


p = Persona(input("Ingrese nombre: "),  int(input("Ingrese edad: ")))

p.cumpleaños()


print(f"{p.nombre} cumple {p.edad} años")

![image](https://github.com/user-attachments/assets/33abb3cd-562c-467f-a198-9751d5d74fe0) ![image](https://github.com/user-attachments/assets/9965117c-8e66-450f-9d1c-d985adb13ce0)

# #3

class Calculadora():

  def __init__(self, num1, num2):
  
  self._num1 = num1
  
  self._num2 = num2

  def suma(self):
  
  resultado = self._num1 + self._num2

  print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

  def resta(self):
  
  resultado = self._num1 - self._num2

  print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}")

  def division(self):

  resultado = self._num1 / self._num2  
  
  print(f"El resultado de la división es: {self._num1} / {self._num2} = {resultado}")

  def multiplicacion(self):

  resultado = self._num1 * self._num2
  
  print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")


operacion = Calculadora(23, 8)

operacion.suma()

operacion = Calculadora(23, 8)

operacion.resta()

operacion = Calculadora(23, 8)

operacion.division()

operacion = Calculadora(23, 8)

operacion.multiplicacion()

![image](https://github.com/user-attachments/assets/15eaa451-ac15-420f-8982-72466a27bebd) ![image](https://github.com/user-attachments/assets/f96b7355-0645-4ce3-bc06-9852335830a5)

# #4

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

![image](https://github.com/user-attachments/assets/48ba6241-d207-431b-9da5-8910f7404658) ![image](https://github.com/user-attachments/assets/1aa3868e-0a5c-4df5-97e9-19ba93b0156d)

# #5

class Fabrica():

  def __init__(self, llantas, color, precio):
   
  self._llantas = llantas
  
  self._color = color
  
  self._precio = precio

class Moto(Fabrica):
  
  def cantidad(self):
  
  print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))


class Carro(Fabrica):
 
  def cantidad(self):
  
  print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
  
  print("OBJETO=carro") 


moto = Moto(2, "Rojo", "$500")

moto.cantidad()


print("OBJETO=carro") 

carro = Carro(4, "Cafe", "$800")

carro.cantidad()

![image](https://github.com/user-attachments/assets/1d21c870-6edb-426c-8412-980619e7c41e) ![image](https://github.com/user-attachments/assets/a9f2f84d-54a0-4a05-a90f-fe5137a2167f)

# #6

class Marino():

  def hablar(self):
  
  print("Hola soy un pollero!")  


class Pulpo(Marino):

  def hablar(self):
  
  print("Hola soy un pollo!")  


class Foca(Marino):

  def hablar(self, mensaje):  
  
  self.mensaje = mensaje
  
  print(mensaje)
 

marino = Marino()

marino.hablar()

pulpo = Pulpo()

pulpo.hablar()

foca = Foca()

foca.hablar("Hola soy una persona que quiere comprar pollo!") 

![image](https://github.com/user-attachments/assets/55b29752-7f86-4d83-95a9-56bd4c395e6f) ![image](https://github.com/user-attachments/assets/a4e9e4d6-6ae0-4119-8527-4cdc80355860)

# #7

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

![image](https://github.com/user-attachments/assets/a580808c-6ffb-43e7-b0b1-051321c80301) ![image](https://github.com/user-attachments/assets/22e2bb42-6abd-4dc8-85d5-b7f0dfd25b6d)


