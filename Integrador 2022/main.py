from ManejadorCamas import arregloCama
from ManejadorMedicamentos import Medicamentos
from ClaseMenu import Menu
if __name__ == '__main__':

#aclaracion ejercicio 8
#igual conjuntos, si  las listas tiene la misma longitud, ordenarlos  y luego compara con el while y luego if.
#union, listas ordenadas y luego 3 for i,j,k para comparar si el numero de la lista 1 es menor a la lista 2 y si es igual
#colocarle un elif. y de ahi agregardo a la nueva lista.
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



