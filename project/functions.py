from constants import constantes
from datetime import date, time, datetime

def array2(paso, MC, CL1, CL2, CL3, CL4, n, ES, maqServer, maqCola):
    paso = paso
    maqCola = maqCola
    maqServer = maqServer
    n = 0
    ES = 0
    MC = 0

    collection = [
        paso, MC, CL1, CL2, CL3, CL4, n, ES, maqServer, maqCola]
    return collection


def returnData(collection):
    for i in range(len(collection)):
        aux = collection[i]
        return aux


# def ValidationOfData(dataCollection, DataMinimun):
#     Out1 = 1001
#     Out2 = 1002
#     Out3 = 1003
#     Out4 = 1004
#     AuxSever = 1
#     for i in range(0, 4):
#         if DataMinimun == dataCollection[2]:
#             dataCollection[1] = DataMinimun
#             dataCollection[2] = Out1
#             dataCollection[5] = dataCollection[1] + 5
#             dataCollection[6] = 1
#             dataCollection[7] = 1
#             dataCollection[8] = AuxSever
#             return dataCollection

def ingresarValoresEnteros(indicacion):
    entrada = input(indicacion)
    if not entrada.isdigit():
        print("\nIngrese un numero entero valido! ")
        entrada = ingresarValores(indicacion)
    return int(entrada)

def guardarEnTxt(texto):
    fecha_hora_actual = datetime.now()
    cadena_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%d_%H:%M:%S")
    nombre = cadena_fecha_hora + '.txt'
    archivo = open(nombre, "w")
    archivo.write(texto)
    archivo.close()