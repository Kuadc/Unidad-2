from ClaseVentana import Ventana


if __name__ == '__main__':
    print('==== Ventana Inicio ====')

    ventanaInicio= Ventana('Inicio')

    ventanaInicio.mostrar()

    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))

    print('\n==== Ventana Cargar ====')

    ventanaCargar= Ventana('Cargar',10,20)

    ventanaCargar.mostrar()

    print('\n*** Mueve a la derecha ***')

    ventanaCargar.moverDerecha(10)

    ventanaCargar.mostrar()

    print('\n*** Mueve a la izquierda ***')

    ventanaCargar.moverIzquierda(10)

    ventanaCargar.mostrar()

    print('\n*** Bajar ***')

    ventanaCargar.bajar(10)

    ventanaCargar.mostrar()

    print('\n\n==== Ventana Borrar ====')

    ventanaBorrar = Ventana('Borrar', 10,20,100,200)

    ventanaBorrar.mostrar()

    print('\n*** Subir ***')

    ventanaBorrar.subir(5)

    ventanaBorrar.mostrar()

    print('\n*** Subir ***')

    ventanaBorrar.subir()

    ventanaBorrar.mostrar()

    print('\n*** Bajar ***')

    ventanaBorrar.bajar()

    ventanaBorrar.mostrar()
