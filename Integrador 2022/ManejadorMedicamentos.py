import csv

from CLaseMedicamento import Medicamento

class Medicamentos():
    __lista =[]

    def __init__(self):
        self.__lista = []

    def AbrirArchivo(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo,delimiter=';')
        Bandera = True
        for fila in reader:
            if Bandera:
                Bandera=False
            else:
                id = int(fila[0])
                med = str(fila[1])
                nomb = str(fila[2])
                mono = str (fila[3])
                pres = str(fila[4])
                cant = int(fila[5])
                precio = int(fila[6])
                unmed = Medicamento(id,med,nomb,mono,pres,cant,precio)
                self.agregarmed(unmed)
        archivo.close()

    def agregarmed(self,unmed):
        self.__lista.append(unmed)

    def __str__(self):
        s = ""
        for fila in self.__lista:
            s+= str(fila) + "\n"

        return s

    def busquedalineal(self,indice):
        posicion = 0
        total=0
        pres="Presentacion"
        cant = "Cantidad"
        pre = "Precio"
        med ="Medicamento"
        mono= "monodroga"
        print("{:<}/{:<15}{:^30}{:^20}{:^15}".format(med,mono,pres,cant,pre))
        while posicion < len(self.__lista):
            if self.__lista[posicion].idcama() == indice:
                print("{:<}/{:<15}{:^30}{:^30}{:.2f}".format(self.__lista[posicion].GetNombre_comer(),self.__lista[posicion].GetMonodroga(),
                                                       self.__lista[posicion].GetPresentacion(),self.__lista[posicion].GetCantidad(),
                                                       self.__lista[posicion].GetPrecio()))
                total+=self.__lista[posicion].GetCantidad()*self.__lista[posicion].GetPrecio()
            posicion = posicion +1
        if posicion > len(self.__lista):
            print("! El Paciente no tiene medicamentos que pagar!")
        else:
            return total
