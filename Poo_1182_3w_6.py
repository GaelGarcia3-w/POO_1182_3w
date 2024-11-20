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
