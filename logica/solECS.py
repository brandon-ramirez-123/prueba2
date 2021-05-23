import math


class EcuacionSegundoGrado():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def SolucionECS(self):
        self.x1 = ""
        self.x2 = ""
        if self.a.isnumeric() and self.b.isnumeric() and self.c.isnumeric():
            a = int(self.a)
            b = int(self.b)
            c = int(self.c)
            d = b * b - 4 * a * c
            if d >= 0:
                r1 = (-b + math.sqrt(d)) / (2 * a)
                r2 = (-b - math.sqrt(d)) / (2 * a)
                self.x1 = "{0:.2f}".format(r1)
                self.x2 = "{0:.2f}".format(r2)
            else:
                d = d * -1
                r1 = (-b) / (2 * a)
                r2 = (math.sqrt(d)) / (2 * a)
                self.x1 = "{0:.2f}".format(r1) + "+" + "{0:.2f}".format(r2) + "i"
                self.x2 = "{0:.2f}".format(r1) + "-" + "{0:.2f}".format(r2) + "i"
            return self.x1, self.x2
        else:
            self.x1 = "ERROR"
            return self.x1, self.x2

    def DefinirParametros(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
