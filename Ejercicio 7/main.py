import csv

from Viajero import ViajeroFrecuente

def AbrirArchivo(unalista):
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
            unalista.append(Unviajero)
    archivo.close()

def CompararViajeros(unalista):
    millas=int(input("Ingrese cantidad de millas para comparar: "))
    encontrado= False
    posicion = 0
    while not (encontrado) and posicion < len(unalista):
        if millas == unalista[posicion]:
            encontrado = True
            return print("El siguiente viajero tiene las mismas millas: ", unalista[posicion])
        posicion = posicion +1

def mostrardatos(unalista):
    for lista in range(len(unalista)):
        print(unalista[lista])

def busquedabinaria(unalista,elem):
    inf = 0
    sup = len(unalista)
    medio = (inf+sup) //2
    encontrado = True
    while inf <=sup and elem != unalista[medio].Getviajero():
        if elem < unalista[medio].Getviajero():
            sup = medio+1

        medio=(inf+sup) //2

    if inf <= sup:
        return medio
    else:
        return -1

def AcumularMillas(unalista):
    elemento = int(input("Ingrese el numero del viajero: "))
    i=busquedabinaria(unalista,elemento)
    if i == -1:
        print("No se encontro el viajero")
    else:
        print("Total de millas acumuladas:", unalista[i].GetMillas())
        millas = int(input("Ingrese la cantidad de millas para acumular: "))
        unalista[i]= millas + unalista[i]
        print("El total nuevo acumulado es: ",unalista[i].GetMillas())

def CanjearMillas(unalista):
    elemento = int(input("Ingrese el numero del viajero: "))
    i=busquedabinaria(unalista,elemento)
    print(unalista[i].GetMillas())
    if i == -1:
        print("No se encontro el viajero")
    else:
        millas = int(input("Ingrese la cantidad de millas para canjear: "))
        if millas < unalista[i].GetMillas():
            unalista[i]= millas - unalista[i]
            print("El total nuevo acumulado es: ",unalista[i].GetMillas())
        else:
            print("No puede canjear millas, cantidad insuficiente")

# _________ Programa principal __________

if __name__ == '__main__':
    unalista= []
    AbrirArchivo(unalista)
    mostrardatos(unalista)
    print()
    CompararViajeros(unalista)
    AcumularMillas(unalista)
    CanjearMillas(unalista)

