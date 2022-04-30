from ClaseLista import ListaPlan
from ClaseMenu import Menu
if __name__ == '__main__':
    Lplan = ListaPlan()
    Lplan.AbrirArchivo()
    unmenu = Menu()
    while True:
        print('\n-------Menu--------')
        print("1) - Actualizar el valor del vehículo de cada plan.")
        print("2) - Mostrar código del plan, modelo y versión del vehículo.")
        print("3) - Total monto para Licitar")
        print("4) - Finalizar")
        opcion= input("\nIngrese la opcion Deseada: ")
        unmenu.opcion(opcion,Lplan)


