from logica.solECS import EcuacionSegundoGrado

if __name__ == '__main__':
    solucion = EcuacionSegundoGrado()

    solucion.DefinirParametros('1', '1', '1')
    x1, x2 = solucion.SolucionECS()

    print(x1)
    print(x2)
