from functions import array2, MinimumData, returnData
from tabulate import tabulate

# Datos a pedir al usuario


dataMinimun = MinimumData(1, 4, 9, 1000)

matriz = [array2(0, 0, 1, 4, 9, 1000, 0, 0, 0, 0)]
Out1 = 1001
Out2 = 1002
Out3 = 1003
Out4 = 1004
AuxServer = 1

for i in range(0, 4):
    print(tabulate(matriz, headers=["PASO", "MC", "CL1",
                                    "CL2", "CL3", "CL4", "n", "ES", "#MaqEnServer",
                                    "#MaqEnCola"], tablefmt="orgtbl"))
    print(" ")
    dataCollection = returnData(matriz)
    # realizar validaciones de los datos aqui
    newDataMinimum = MinimumData(
        dataCollection[2], dataCollection[3], dataCollection[4], dataCollection[5])
    print(newDataMinimum)
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
    if newDataMinimum == dataCollection[4]:
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
