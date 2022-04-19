import csv
import numpy as np
from Email import ClaseEmail

class arregloNumpy:
    def __init__(self, dimension, incremento = 5):
        self.__emails = np.empty(dimension,dtype=ClaseEmail)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
    def agregarEmail(self,unmail):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__emails.resize(self.__dimension)
        self.__emails[self.__cantidad]=unmail
        self.__cantidad += 1

    def ManejadorArchivo(self):
        archivo = open("lista.csv")
        datos = csv.reader(archivo, delimiter=',')
        y=0
        print("\n------Comienza la carga de obejtos en el arreglo------\n")
        for x in datos:
            if y==0:
             p1 = ClaseEmail()
             mail = x[y]
             p1.crearcuenta(mail)
             self.agregarEmail(p1)

        print("\n------Emails guardados en el arreglo------\n")
        archivo.close()

    def mostraremails(self):
        for i in range(self.__cantidad):
            self.__emails[i].mostrarDatos()



    def buscarEmail(self):
        unmail = input("Ingrese el ID a buscar: ")
        y=0
        for i in range(self.__cantidad):
            indice=self.__emails[i].CompararDatos(unmail)
            if indice == 1:
                y+=1

        if y >= 2:
            print("El id {} esta repetido {} veces",unmail,y)
        else:
            print("El id No esta repetido")
