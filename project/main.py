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
    "ES": "Desocupado",
    "maqServer": "-",
    "maqCola": "-"
}
    
    #* Guardamos las filas de la matriz a imprimir la final
filas = [tuple(valores.values())]


for i in range(0, 15):    
    
    clocksAuxiliar = [valores["clock1"], valores["clock2"],valores["clock3"],valores["clock4"],valores["clock5"]]
    valores["MC"] = min(clocksAuxiliar)

    for element in out:
        if not element in clocksAuxiliar:
            #Si el clock auxiliar es el minimo
            if clocksAuxiliar.index(min(clocksAuxiliar)) == (len(clocksAuxiliar) - 1):
                if clocksAuxiliar[len(clocksAuxiliar) - 1] == valores["MC"]:
                    clocksAuxiliar[len(clocksAuxiliar) - 1] = valores["MC"] + 11
                
                if clocksAuxiliar[len(clocksAuxiliar) - 1] != 1000:
                    clocksAuxiliar[clocksAuxiliar.index(out[0])] = valores["MC"] + 480
                break
            
            #Se asigna si el reloj auxiliar index
            clocksAuxiliar[clocksAuxiliar.index(min(clocksAuxiliar))] = element
            valores["ES"] = "Ocupado"

            #Si el elemento es el primer out
            if element == out[0]:
                clocksAuxiliar[len(clocksAuxiliar) - 1] = valores["MC"] + 11
            break
    
    if not out[0] in clocksAuxiliar:
        contador = 0
        for i in range(1,len(out)):
            if out[i] in clocksAuxiliar:
                clocksAuxiliar[clocksAuxiliar.index(out[i])] = out[i-1]
                contador += 1
        if contador == 0:
            clocksAuxiliar[len(clocksAuxiliar) - 1] = 1000
            valores["ES"] = "Desocupado"

    valores["numero"] = 0
    # * Obtenemos el numero
    for element in out:
        if element in clocksAuxiliar:
            valores["numero"] += 1

    # * Obtenemos la maquina en servicio
    if out[0] in clocksAuxiliar:
        valores["maqServer"] = clocksAuxiliar.index(out[0]) + 1
    else:
        valores["maqServer"] = "-"
    
    # * Obtenemos la maquina en cola
    if out[1] in clocksAuxiliar:
        valores["maqCola"] = clocksAuxiliar.index(out[1]) + 1
    else:
        valores["maqCola"] = "-"
    
    
    # * Actualizando los valores
    valores["clock1"] = clocksAuxiliar[0]
    valores["clock2"] = clocksAuxiliar[1]
    valores["clock3"] = clocksAuxiliar[2]
    valores["clock4"] = clocksAuxiliar[3]
    valores["clock5"] = clocksAuxiliar[4]
    
    valores["Paso"]+=1
    if valores["clock5"] != valores["MC"]:
        filas.append(tuple(valores.values()))
    else:
        valores["Paso"] -= 1

    
print("\n")
print(tabulate(filas, headers=list(valores.keys()), tablefmt="orgtbl"))


# guardarEnTxt(tabulate(filas, headers=list(valores.keys()), tablefmt="orgtbl"))
