from functions import array2, returnData, ingresarValoresEnteros, guardarEnTxt
from tabulate import tabulate

#Variables
texto = ""

# Datos a pedir al usuario
#Pedimos los clocks
clock1 = ingresarValoresEnteros("Ingrese el clock 1:\n")
clock2 = ingresarValoresEnteros("Ingrese el clock 2:\n")
clock3 = ingresarValoresEnteros("Ingrese el clock 3:\n")
clock4 = ingresarValoresEnteros("Ingrese el clock 4:\n")
#Ingresamos todos los clocks en una sola variable
clocks = [clock1, clock2, clock3, clock4]






dataMinimun = min(clocks)

matriz = [array2(0, 0, clock1, clock2, clock3, clock4, 0, 0, 0, 0)]
Out1 = 1001
Out2 = 1002
Out3 = 1003
Out4 = 1004
AuxServer = 1

for i in range(0, 4):
    print(tabulate(matriz, headers=["PASO", "MC", "CL1",
                                    "CL2", "CL3", "CL4", "n", "ES", "#MaqEnServer",
                                    "#MaqEnCola"], tablefmt="orgtbl"))
    texto += tabulate(matriz, headers=["PASO", "MC", "CL1", "CL2", "CL3", "CL4", "n", "ES", "#MaqEnServer","#MaqEnCola"], tablefmt="orgtbl")

    print(" ")
    texto += " "

    dataCollection = returnData(matriz)
    # realizar validaciones de los datos aqui
    newDataMinimum = min(
        dataCollection[2], dataCollection[3], dataCollection[4], dataCollection[5])
    
    print(newDataMinimum)
    texto += str(newDataMinimum) + "\n\n"

    if dataMinimun == dataCollection[2]:
        dataCollection[1] = dataMinimun
        dataCollection[2] = Out1
        dataCollection[5] = dataCollection[1] + 5
        dataCollection[6] = 1
        dataCollection[7] = 1
        dataCollection[8] = AuxServer
    if newDataMinimum == dataCollection[3]:
        dataCollection[1] = dataMinimun
        dataCollection[2] = 151515151515
        dataCollection[5] = dataCollection[1] + 5
        dataCollection[6] = 1
        dataCollection[7] = 1
        dataCollection[8] = AuxServer

    # data1 = MinimumData(array[2], array[3], array[4], array[5])

    # NewMatriz = array2(array[0], array[1], array[2], array[3],
    #                     array[4], array[5], array[6], array[7], array[8], array[9])
    # matriz = [NewMatriz]


guardarEnTxt(texto)