import  csv
from ClaseObjeto import  objeto

class ListaRegistro():
    __lista = []

    def __init__(self):
        self.__lista = []

    def __str__(self):
        s=""
        for listaregistro in self.__lista:
            for columna in listaregistro:
               s += str(columna) + '\n'
        return s

    def AgregarDatos(self,dia, hora,unobjeto):
        self.__lista[dia-1][hora-1]= unobjeto

    def Abrir_Archivo(self):
        self.__lista =[[ 0 for colum in range(24)]for fila in range(3)]
        archivo = open('registro.csv')
        reader = csv.reader(archivo,delimiter=';')
        Bandera = True
        for fila in reader:
            if Bandera:
                Bandera = False
            else:
                dia = int(fila[0])
                hora = int(fila[1])
                temp = int(fila[2])
                hum = int(fila[3])
                presion = int(fila[4])
                Unobjeto = objeto(temp,hum,presion)
                self.AgregarDatos(dia,hora,Unobjeto)
        archivo.close()

    def GetPresion(self):
        mayor=0
        maxbandera=0
        menor=999
        minbandera=0
        for i in range(len(self.__lista)): # La cantidad de filas
            for j in range(len(self.__lista[i])): # La cantidad que tiene cada fila
                maximo = self.__lista[i][j].GetItem_presion()
                if maximo > mayor:
                   mayor=maximo
                   maxbandera=i
                if maximo <menor:
                    menor=maximo
                    minbandera=i
        print("El dia {} tubvo la mayor Presion {}".format(maxbandera+1,mayor))
        print("El dia {} tuvo la menor Presion y fue de {}" .format(minbandera+1,menor))

    def GetTemp(self):
        mayor=0
        maxbandera=0
        menor=999
        minbandera=0
        for i in range(len(self.__lista)): # La cantidad de filas
            for j in range(len(self.__lista[i])): # La cantidad que tiene cada fila
                maximo = self.__lista[i][j].GetItem_temp()
                if maximo > mayor:
                   mayor=maximo
                   maxbandera=i
                if maximo <menor:
                    menor=maximo
                    minbandera=i
        print("El dia {} tubvo la mayor Temperatura {}".format(maxbandera+1,mayor))
        print("El dia {} tuvo la menor Temperatura y fue de {}" .format(minbandera+1,menor))

    def GetHum(self):
        mayor=0
        maxbandera=0
        menor=999
        minbandera=0
        for i in range(len(self.__lista)): # La cantidad de filas
            for j in range(len(self.__lista[i])): # La cantidad que tiene cada fila
                maximo = self.__lista[i][j].GetItem_hum()
                if maximo > mayor:
                   mayor=maximo
                   maxbandera=i
                if maximo <menor:
                    menor=maximo
                    minbandera=i
        print("El dia {} tubvo la mayor Humedad {}".format(maxbandera+1,mayor))
        print("El dia {} tuvo la menor Humedad y fue de {}" .format(minbandera+1,menor))

    def TempMensual(self):
        totaltemp=0

        for j in range(24):
            for i in range(3): # La cantidad de filas
                # La cantidad que tiene cada fila
                maximo = self.__lista[i][j].GetItem_temp()
                totaltemp+=maximo
            totaltemp/=3
            print("El para la hora {} la mayor temperatura fue de {:.2f}".format(j+1,totaltemp))
    def Getdia(self):
        dia=int(input("Ingrese el dia:"))
        h="Hora"
        t= "Temperatura"
        hu="Humedad"
        p= "Presion"
        print("{:>15}{:>15}{:>15}{:>15}".format(h,t,hu,p))
        for i in range(dia):
            for j in range(24):
                print("{:>13}{:>13}{:>15}{:>15}".format(j+1,self.__lista[i][j].GetItem_temp(),self.__lista[i][j].GetItem_hum(),self.__lista[i][j].GetItem_presion()))


