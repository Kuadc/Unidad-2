from ManejadorCamas import arregloCama
from ManejadorMedicamentos import Medicamentos

from ClaseCamas import Cama
from CLaseMedicamento import Medicamento

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.salir}

    def opcion(self,op,arre,med):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2':
            func(arre,med)
        else:
            func()

    def opcion2(self,arre,med):
        #Listar los datos de pacientes internados (cama ocupada) Neumonitis
        cad = input("Ingrese el diagnostico: ")
        arre.buscarcama(cad)

    def opcion1(self,arre,med):
        #Listar los datos del paciente y los medicamentos
        cadena = str(input("Ingrese el nombre y apellido del paciente: "))
        print()
        indice = arre.busquedalineal(cadena)
        print(indice)
        if indice == -1:
            print("! Paciente no encontrado, intente nuevamente!")
        else:
            print()
            total=med.busquedalineal(indice)
            print("Total adeudado:                                                                        {:.2f}".format(total))



    def salir(self):
        exit()
