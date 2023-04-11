from functions import guardarEnTxt, valoresDeUnDiccionario, cargarDatos
from tabulate import tabulate

# Variables

## Datos a pedir al usuario
### Pedimos los clocks (1-4)
# clocks = cargarDatos()
clocks = [53, 5, 14, 31]

    
    #* Clock 5
clockAuxiliar = 1000
    #* Clock 5

## Datos del sistema
out = [1001, 1002, 1003, 1004, 1005]
AuxOut = 0
AuxServer = 1
valores = {
    "Paso" : 0,
    "MC": 0,
    "clock1": clocks[0],
    "clock2": clocks[1],
    "clock3": clocks[2],
    "clock4": clocks[3],
    "clock5": clockAuxiliar,
    'numero': 0,
    "ES": 0,
    "maqServer": 0,
    "maqCola": 0
}
    
    #* Guardamos las filas de la matriz a imprimir la final
filas = [tuple(valores.values())]


for i in range(0, 10):
    """ clocksAuxiliar = clocks
    clocksAuxiliar.append(clockAuxiliar) """
    
    clocksAuxiliar = [valores["clock1"], valores["clock2"],valores["clock3"],valores["clock4"],valores["clock5"]]
    valores["MC"] = min(clocksAuxiliar)


    for element in out:
        if not element in clocks:
            if clockAuxiliar == 1000:
                clockAuxiliar = clocksAuxiliar[clocksAuxiliar.index(min(clocksAuxiliar))] + 11
            clocks[clocks.index(min(clocks))] = element
            valores["ES"] = 1
            break
        
    if valores["MC"] == clockAuxiliar:
        clocks[clocks.index(min(out))] = valores["MC"] + 480
        for i in range(1,4):
            if out[i] in clocks:
                clocks[clocks.index(out[i])] = out[i-1]
    
    # * Actualizando los valores
    valores["clock1"] = clocks[0]
    valores["clock2"] = clocks[1]
    valores["clock3"] = clocks[2]
    valores["clock4"] = clocks[3]
    valores["clock5"] = clockAuxiliar
    
    valores["Paso"]+=1
    filas.append(tuple(valores.values()))

    
print("\n")
print(tabulate(filas, headers=list(valores.keys()), tablefmt="orgtbl"))


# guardarEnTxt(tabulate(filas, headers=list(valores.keys()), tablefmt="orgtbl"))
