import math


class EcuacionSegundoGrado():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def SolucionECS(self):
        self.x1 = ""
        self.x2 = ""
        d = self.b * self.b - 4 * self.a * self.c
        if d >= 0:
            r1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            r2 = (-self.b - math.sqrt(d)) / (2 * self.a)
            self.x1 = "{0:.2f}".format(r1)
            self.x2 = "{0:.2f}".format(r2)
        else:
            r1 = (-self.b) / (2 * self.a)
            r2 = (math.sqrt(-d)) / (2 * self.a)
            self.x1 = "{0:.2f}".format(r1) + "+" + "{0:.2f}".format(r2) + "i"
            self.x2 = "{0:.2f}".format(r1) + "-" + "{0:.2f}".format(r2) + "i"
        return self.x1, self.x2

    def DefinirParametros(self, a, b, c):
        self.a = self.ParametroAFloat(a)
        self.b = self.ParametroAFloat(b)
        self.c = self.ParametroAFloat(c)

    def ImprimirSolucion(self):
        print("Ecuacion de segundo grado:")
        print(str(self.a)+"x^2 + "+str(self.b)+"x + "+str(self.c))
        print("\nSolucion:")
        print("X1 = " + self.x1)
        print("X2 = " + self.x2)

    def ParametroAFloat (self, parametro):
        if not type(parametro) is float:
            try:
                parametro=float(parametro)
            except ValueError:
                print(f"El parametro: \"{parametro}\" no se puede converir a float")
                exit(1)
        return parametro