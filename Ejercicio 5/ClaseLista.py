import csv

from ClasePlanAhorro import PlanAhorro

class ListaPlan():
    __lista=[]

    def __init__(self):
        self.__lista =[]

    def agregarplan(self,unplan):
        self.__lista.append(unplan)

    def __str__(self):
        s='Codigo Modelo Version Valor'
        for plan in self.__lista:
            s+= str(plan) + '\n'
        return s

    def Cambiarvalor(self):
        for plan in range(len(self.__lista)):
            print(self.__lista[plan])
            valor = float(input("Ingrese el valor del vehiculo: "))
            self.__lista[plan].Getvalor2(valor)

    def mostrarvalores(self):
        #valor cuota = (importe vehículo/ cantidad de cuotas) + importe vehículo * 0.10
        valor = float(input("Ingrese el valor a buscar: "))
        for plan in range(len(self.__lista)):
            importe = self.__lista[plan].Getvalor()
            cuotas = PlanAhorro.GetCant_Cuotas()
            valor_cuota= (importe/cuotas) + importe * 0.10
            if valor_cuota < valor:
                print("El plan con la cuota ingresada es el siguiente:")
                print("Codigo del plan:{} \n Modelo :{} \n Version:{} ".format(self.__lista[plan].Getcodigo(),self.__lista[plan].Getmodelo(),self.__lista[plan].Getversion()))

    def AbrirArchivo(self):
        archivo = open('Planes.csv')
        reader = csv.reader(archivo,delimiter=';')
        Bandera = True
        for fila in reader:
            if Bandera:
                Bandera=False
            else:
                cod= int(fila[0])
                mod = int(fila[1])
                ver = int (fila[2])
                valor = float(fila[3])
                unplan = PlanAhorro(cod,mod,ver,valor)
                self.agregarplan(unplan)
        archivo.close()

    def Valorcuota(self,valor):
        #valor cuota = (importe vehículo/ cantidad de cuotas) + importe vehículo * 0.10
        valor_cuota = self.__lista
        return

    def MostrarLicitacion(self):
        plan = int(input("Ingrese codigo del plan:"))
        for planes in range(len(self.__lista)):
            if plan == self.__lista[planes].Getcodigo():
                importe = self.__lista[planes].Getvalor()
                cuotas = PlanAhorro.GetCant_Cuotas()
                valor_cuota= (importe/cuotas) + importe * 0.10
                total_licitacion = valor_cuota * PlanAhorro.GetCant_Cuotaspagas()
                print("La cantidad para licitar del plan {}, es de: ${}".format(plan,total_licitacion))
