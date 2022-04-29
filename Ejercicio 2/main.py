from DataViajero import ListaViajero
from claseMenu import Menu

if __name__ == '__main__':
    vf = ListaViajero()
    vf.Abrir_Archivo()
    print("Lista de Viajeros Frecuentes \n")
    print(vf)
    numeroid = int(input("\n Ingrese Numero de Identificacion de Viajero: "))
    indice= vf.buscarviajero(numeroid)
    if indice == None:
        print("resultado no encontrado")
    else:
        opcionmenu = Menu()
        while True:
            print('\n-------Menu--------')
            print("1) - Consultar Cantidad de Millas.")
            print("2) - Acumular Millas.")
            print("3) - Canjear Millas")
            print("4) - Finalizar")
            opcion= input("\nIngrese la opcion Deseada: ")
            opcionmenu.opcion(opcion,vf,indice)



