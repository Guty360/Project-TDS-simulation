from functions import guardarEnTxt, valoresDeUnDiccionario, cargarDatos
from tabulate import tabulate

# Variables

## Datos a pedir al usuario
### Pedimos los clocks (1-4)
clocks = cargarDatos()
    
    #* Clock 5
clocks.append(1000)
    #* Clock 5

## Datos del sistema
Out = [1001, 1002, 1003, 1004, 1005]
AuxOut = 0
AuxServer = 1
valores = {
    "Paso" : 0,
    "MC": 0,
    "clock1": clocks[0],
    "clock2": clocks[1],
    "clock3": clocks[2],
    "clock4": clocks[3],
    "clock5": clocks[4],
    'numero': 0,
    "ES": 0,
    "maqServer": 0,
    "maqCola": 0
}
    
    #* Guardamos las filas de la matriz a imprimir la final
filas = []

dataMinimun = min(clocks)

for i in range(0, 4):
    
    filas.append(tuple(valores.values()))
    
    #Tomamos el valor minimo
    newDataMinimum = min(valores["clock1"], valores["clock2"], valores["clock3"], valores["clock4"], valores["clock5"])

    # ----------> CL1 <----------
    if dataMinimun == valores["clock1"]:
        if valores["MC"] == valores["numero"]:
            AuxOut = valores["MC"] + 10
        else:
            AuxOut = Out[0]
        valores["MC"] = dataMinimun
        valores["clock1"] = AuxOut
        valores["numero"] = valores["MC"] + 5
        valores["ES"] = 1
        valores["maqServer"] = 1
        valores["maqCola"] = AuxServer


    # ----------> CL2 <----------
    if newDataMinimum == valores["clock2"]:
        if valores["MC"] == valores["clock4"]:
            AuxOut = valores["MC"] + 10
            AuxOut2 = valores["clock4"] + 5
        else:
            AuxOut = Out[0]
            AuxOut2 = valores["clock4"]

        valores["MC"] = newDataMinimum
        valores["clock1"] = AuxOut
        valores["clock2"] = Out[1]
        valores["numero"] = AuxOut2
        valores["ES"] = 1
        valores["maqServer"] = 1
        valores["maqCola"] = AuxServer
    
    # ----------> CL3 <----------
    if newDataMinimum == valores["clock3"]:
        if valores["MC"] == valores["clock4"]:
            AuxOut = valores["MC"] + 10
            AuxOut2 = valores["clock4"] + 5
        else:
            AuxOut = valores["MC"] + 10
        valores["MC"] = newDataMinimum
        valores["clock1"] = AuxOut
        valores["clock2"] = Out[0]
        valores["numero"] = AuxOut2
        valores["ES"] = 1
        valores["maqServer"] = 1
        valores["maqCola"] = AuxServer
     
     # ----------> CL4 <----------
    if newDataMinimum == valores["clock4"]:
        if valores["MC"] == valores["clock4"]:
            AuxOut = valores["MC"] + 10
            AuxOut2 = valores["clock4"] + 5
        else:
            AuxOut = Out4
        valores["MC"] = newDataMinimum
        valores["clock1"] = valores["MC"] + 10
        valores["clock2"] = Out[3]
        valores["clock3"] = Out[3]
        valores["numero"] = AuxOut2
        valores["ES"] = 1
        valores["maqServer"] = 1
        valores["maqCola"] = AuxServer
    
print("\n")
print(tabulate(filas, headers=list(valores.keys()), tablefmt="orgtbl"))


# guardarEnTxt(tabulate(filas, headers=list(valores.keys()), tablefmt="orgtbl"))
