import csv

import numpy as np
from ClaseCamas import Cama


class arregloCama:
    def __init__(self, dimension, incremento = 5):
        self.__camas = np.empty(dimension,dtype=Cama)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
    def agregarcama(self,unacama):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__camas.resize(self.__dimension)
        self.__camas[self.__cantidad]=unacama
        self.__cantidad += 1

    def ManejadorArchivo(self):
        archivo = open("camas.csv")
        datos = csv.reader(archivo, delimiter=';')
        Bandera = True
        print("\n------Comienza la carga de objetos en el arreglo------\n")
        for x in datos:
            if Bandera:
                Bandera = not Bandera
                #Salteamos los titulos del archivo
            else:
                cama = int(x[0])
                hab = int(x[1])
                est = bool(x[2])
                ayn = x[3]
                diag = x[4]
                fint = str(x[5])
                falt = x[6]
                p1 = Cama(cama,hab,est,ayn,diag,fint,falt)
                self.agregarcama(p1)
        archivo.close()

    def mostrarcamas(self):
        for i in range(self.__cantidad):
            print(self.__camas[i])

    def busquedalineal(self,cadena):
        encontrado= False
        posicion = 0
        while not encontrado and posicion < len(self.__camas):
            if self.__camas[posicion].Getnombre() == cadena:
                self.__camas[posicion].DardeAlta()
                self.__camas[posicion].Mostrarpaciente()
                encontrado = True
            posicion = posicion +1
        if posicion > len(self.__camas):
            return -1
        else:
            return posicion

    def buscarcama(self,cadena):
        encontrado= False
        posicion = 0
        while not encontrado and posicion < len(self.__camas):
            if self.__camas[posicion].Getdiag() == cadena:
                self.__camas[posicion].Mostrarpaciente()
                encontrado = True
            posicion = posicion +1
        if posicion == len(self.__camas):
            print("! Paciente no encontrado, intente nuevamente!")
