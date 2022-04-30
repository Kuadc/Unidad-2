from ClaseLista import ListaPlan

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }

    def opcion(self,op,lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3":
            func(lista)
        else:
            func()

    def salir(self):
        print('Usted salio del programa')


    def opcion1(self,lista):
        #cambiar el valor de cada vehiculo
        lista.Cambiarvalor()

    def opcion2(self,lista):
        #Mostrar valor inferiores
        lista.mostrarvalores()

    def opcion3(self,lista):
        #Monto para licitar
        lista.MostrarLicitacion()

    def salir(self):
        exit()
