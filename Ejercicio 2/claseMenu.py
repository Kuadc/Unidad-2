from Viajero import ViajeroFrecuente
from DataViajero import ListaViajero

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }

    def opcion(self,op,vf,indice):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=="3":
            func(vf,indice)
        else:
            func()

    def salir(self):
        print('Usted salio del programa')


    def opcion1(self,vf,indice):
        #Consultar Millas acumuladas
        print("Consultar millas")
        print(vf[indice])  #llamamos a __getitem__ y nos devuelve el objeto del indice

    def opcion2(self,vf,indice):
        #Acumular Millas
        print("Acumular millas")
        millas=int(input("Ingrese la cantidad de millas: "))
        Totalmillas = vf[indice]+millas
        print("* Nueva cantidad de millas acumuladas es: ",Totalmillas)

    def opcion3(self,vf,indice):
        #Canjear millas
        print("* Canjear millas * ")
        millas = int(input("Ingrese la cantidad de millas a canjear: "))
        if vf[indice] <millas:
            print("Millas insuficientes, intente nuevamente")
        else:
            totalmillas=vf[indice]-millas
            print("¡Cambio de millas Satisfactorio!")
            print("El nuevo total de millas es: ",totalmillas)

    def salir(self):
        exit()
