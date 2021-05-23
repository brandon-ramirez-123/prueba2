from logica.solECS import EcuacionSegundoGrado

if __name__ == '__main__':
    solucion = EcuacionSegundoGrado()
    solucion.DefinirParametros('1', '2', '3')
    x1, x2 = solucion.SolucionECS()
    solucion.ImprimirSolucion()
