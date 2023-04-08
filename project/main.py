from functions import array2, MinimumData
from constants import setDefaultData
from tabulate import tabulate

# Datos a pedir al usuario


data = MinimumData(1, 4, 9, 1000)

matriz = [array2(data, 1, 4, 9, 1000)]

for i in range(0, 4):
    print(tabulate(matriz, headers=["PASO", "MC", "CL1",
                                    "CL2", "CL3", "CL4", "n", "ES", "#MaqEnServer",
                                    "#MaqEnCola"], tablefmt="orgtbl"))
    print(" ")
    data1 = MinimumData(45, 5, 45, 120)
    NewMatriz = array2(data1, 4, 5, 45, 120)
    matriz = [NewMatriz]
