import csv
from Viajero import ViajeroFrecuente

class ListaViajero:
    __lista = []

    def __init__(self):
        self.__lista = []

    def AgregarViajero(self,Unviajero):
        self.__lista.append(Unviajero)

    def __str__(self):
        s = "ID DNI Apellido    Nombre  MIllas \n"
        for viajero in self.__lista:
            s += str(viajero) + '\n'
        return s

    def buscarviajero(self,numero):
        for indice, viajero in enumerate(self.__lista):
            if viajero.Getviajero() == numero:
                return  indice

    def __getitem__(self, item):
        return self.__lista[item][4]

    def Acumularmillas(self,indice,millas):
        self.__lista[item][4]+=millas


    def Abrir_Archivo(self):
        archivo = open("viajeros.csv")
        reader = csv.reader(archivo,delimiter = ";")
        bandera = True
        for fila in reader:
            if bandera:
            #'''saltear cabecera '''
             bandera = not bandera
            else:
             viajero = int(fila[0])
             dni = fila[1]
             nom = fila[2]
             ape = fila[3]
             millas = int(fila[4])
             Unviajero = ViajeroFrecuente(viajero, dni, nom, ape,millas)
             self.AgregarViajero(Unviajero)
        archivo.close()









