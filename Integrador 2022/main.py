from ManejadorCamas import arregloCama
from ManejadorMedicamentos import Medicamentos
from ClaseMenu import Menu
if __name__ == '__main__':
    arre = arregloCama(3,2)
    arre.ManejadorArchivo()
    arre.mostrarcamas()
    print()
    print("____Lista de Medicamentos cargados____\n")
    med = Medicamentos()
    med.AbrirArchivo()
    print(med)
    unmenu = Menu()
    while True:
        print('\n-------Menu--------')
        print("1) - Listar los datos del paciente y los medicamentos.")
        print("2) - Listar los datos de pacientes internados (cama ocupada).")
        print("3) - Finalizar")
        opcion= input("\n Ingrese la opcion Deseada: ")
        unmenu.opcion(opcion,arre,med)
