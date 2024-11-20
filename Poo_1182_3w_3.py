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
