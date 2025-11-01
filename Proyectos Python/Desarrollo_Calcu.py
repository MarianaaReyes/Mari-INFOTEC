class Calculadora:
    def __init__(self):
        self._numeros = []
        self._historial = []

    # Método para asignar lista de números
    def asignar_numeros(self, lista):
        self._numeros = lista

    # Suma de todos los valores
    def sumar(self):
        resultado = sum(self._numeros)
        operacion = " + ".join(map(str, self._numeros)) + f" = {resultado}"
        self.agregar_a_historial(operacion)
        return resultado

    # Resta desde el primer número
    def restar(self):
        resultado = self._numeros[0]
        for num in self._numeros[1:]:
            resultado -= num
        operacion = " - ".join(map(str, self._numeros)) + f" = {resultado}"
        self.agregar_a_historial(operacion)
        return resultado

    # Multiplicación de todos los valores
    def multiplicar(self):
        resultado = 1
        for num in self._numeros:
            resultado *= num
        operacion = " * ".join(map(str, self._numeros)) + f" = {resultado}"
        self.agregar_a_historial(operacion)
        return resultado

    # División progresiva
    def dividir(self):
        resultado = self._numeros[0]
        try:
            for num in self._numeros[1:]:
                resultado /= num
            operacion = " / ".join(map(str, self._numeros)) + f" = {resultado}"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir entre cero."
            operacion = resultado

        self.agregar_a_historial(operacion)
        return resultado

    # Potencia: toma solo los dos primeros
    def potencia(self):
        if len(self._numeros) == 2:
            resultado = self._numeros[0] ** self._numeros[1]
            operacion = f"{self._numeros[0]} ^ {self._numeros[1]} = {resultado}"
        else:
            resultado = "Error: La potencia solo usa 2 números (base ^ exponente)."
            operacion = resultado

        self.agregar_a_historial(operacion)
        return resultado

    # Historial
    def ver_historial(self):
        print("\n HISTORIAL DE OPERACIONES ")
        if not self._historial:
            print("Historial vacío.\n")
        else:
            for operacion in self._historial:
                print(operacion)
            print()

    def agregar_a_historial(self, operacion):
        self._historial.append(operacion)


def interpretar_expresion(expresion):
    """Devuelve lista de números y el operador detectado"""
    for operador in ['+', '-', '*', '/', '^']:
        if operador in expresion:
            partes = expresion.split(operador)
            try:
                numeros = [float(x.strip()) for x in partes]
                return numeros, operador
            except ValueError:
                return None
    return None


def main():
    calc = Calculadora()
    print(" CALCULADORA CON MÚLTIPLES NÚMEROS ")
    print("Puedes realizar operaciones como: 2 + 3 + 5, 10 * 2 * 3, 2 ^ 3")
    print("Escribe 'historial' para ver tus operaciones o 'salir' para terminar.\n")

    while True:
        print(" Ingrese la operación:")
        entrada = input("➡  ")

        if entrada.lower() == "salir":
            print("\n¡Hasta pronto! ")
            break

        if entrada.lower() == "historial":
            calc.ver_historial()
            continue

        resultado = interpretar_expresion(entrada)
        if not resultado:
            print(" Expresión no válida. Usa formato: número operador número...\n")
            continue

        numeros, operador = resultado
        calc.asignar_numeros(numeros)

        print("\n Resultado:")
        if operador == '+':
            print(calc.sumar(), "\n")
        elif operador == '-':
            print(calc.restar(), "\n")
        elif operador == '*':
            print(calc.multiplicar(), "\n")
        elif operador == '/':
            print(calc.dividir(), "\n")
        elif operador == '^':
            print(calc.potencia(), "\n")


if __name__ == "__main__":
    main()