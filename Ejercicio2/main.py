from DataRegistro import ListaRegistro
from ClaseObjeto import  objeto



def opcion1(unlista):
        #Mostrar para cada variable el día y hora de menor y mayor valor
    print("PRESION")
    unlista.GetPresion()
    print("\nTEMPERATURA")
    unlista.GetTemp()
    print("\nHumedad")
    unlista.GetHum()

def opcion2(unlista):
    #indicar la temperatura promedio mensual
    unlista.TempMensual()

def opcion3(unlista):
    #para un dia dado mostrar la iformacion de las 3 variables
    unlista.Getdia()
    pass


def salir():
        exit()
switcher = {'1':opcion1,
            '2':opcion2,
            '3':opcion3,
            '4':salir}

def opcion(op,unlista):
    func=switcher.get(op, lambda: print("Opción no válida"))
    if op=='1' or op=='2' or op=="3":
        func(unlista)
    else:
        func()
# Programa principal
if __name__ == '__main__':
    unlista = ListaRegistro()
    unlista.Abrir_Archivo()
    print("Lista Cargada",unlista)
    while True:
        print("-----Menu de opciones------")
        print("1) Mostrar para cada variable el día y hora de menor y mayor valor")
        print("2) Indicar la temperatura promedio mensual por cada hora")
        print("3) Dado un número de día listar los valores de las tres variables")
        print("4) Salir")
        op = input("\n Ingrese la opcion Deseada: ")
        opcion(op,unlista)
        break
