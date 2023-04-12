from functions import guardarEnTxt, cargarDatos
from tabulate import tabulate
import json

# Variables
ajuste = {
    "tiempoSeteoYAjuste" : 11,
    "tiempoNormalDeUsoDeMaquina" : 480,
    "cantidadDeEjecucciones" : 25
}


## Datos a pedir al usuario
### Pedimos los clocks (1-4)
clocks = cargarDatos()

    
#* Clock del servidor
clockServidor = 10000

## Datos del sistema
out = [10001, 10002, 10003, 10004, 10005]
valores = {
    "Paso" : 0,
    "MC": 0,
}

for i, clock in enumerate(clocks):
    key = "clock{}".format(i+1)
    valores[key] = clock
#Agregamos el clock servidor
key = "clock{}".format(len(clocks)+1)
valores[key] = clockServidor

valores['numero']= 0
valores["ES"]= "Desocupado"
valores["maqServer"]= "-"
valores["maqCola"]= "-"

    
#* Guardamos las filas de la matriz a imprimir la final
filas = [tuple(valores.values())]


for i in range(0, ajuste["cantidadDeEjecucciones"]):    
    
    clocksAuxiliar = []
    for i in range(0, len(clocks)+1):
        clocksAuxiliar.append(valores["clock{}".format(i+1)])

    valores["MC"] = min(clocksAuxiliar)

    for element in out:
        if not element in clocksAuxiliar:
            #Si el clock auxiliar es el minimo
            if clocksAuxiliar.index(min(clocksAuxiliar)) == (len(clocksAuxiliar) - 1):
                if clocksAuxiliar[len(clocksAuxiliar) - 1] == valores["MC"]:
                    clocksAuxiliar[len(clocksAuxiliar) - 1] = valores["MC"] + ajuste["tiempoSeteoYAjuste"]
                
                if clocksAuxiliar[len(clocksAuxiliar) - 1] != clockServidor:
                    clocksAuxiliar[clocksAuxiliar.index(out[0])] = valores["MC"] + ajuste["tiempoNormalDeUsoDeMaquina"]
                break
            
            #Se asigna si el reloj auxiliar index
            clocksAuxiliar[clocksAuxiliar.index(min(clocksAuxiliar))] = element
            valores["ES"] = "Ocupado"

            #Si el elemento es el primer out
            if element == out[0]:
                clocksAuxiliar[len(clocksAuxiliar) - 1] = valores["MC"] + ajuste["tiempoSeteoYAjuste"]
            break
    
    if not out[0] in clocksAuxiliar:
        contador = 0
        for i in range(1,len(out)):
            if out[i] in clocksAuxiliar:
                clocksAuxiliar[clocksAuxiliar.index(out[i])] = out[i-1]
                contador += 1
        if contador == 0:
            clocksAuxiliar[len(clocksAuxiliar) - 1] = clockServidor
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
    for i in range(1, len(clocksAuxiliar)+1):
        valores["clock{}".format(i)] = clocksAuxiliar[i-1]
    
    valores["Paso"]+=1
    # Para los casos especiales cuando al momento de salida y entrada coincida y se muestran dos Master Clock "MC" con el mismo el valor, es que se usa este y solo imprime una vez el master clock
    if valores["clock{}".format(len(clocksAuxiliar))] != valores["MC"]:
        filas.append(tuple(valores.values()))
    else:
        valores["Paso"] -= 1

    
print("\n")
print("Los ajustes usados son:")
print(ajuste)
print("\n")
print(tabulate(filas, headers=list(valores.keys()), tablefmt="orgtbl"))

txt += "Los ajustes usados son:\n"
txt += json.dumps(ajuste)
txt += "\n\n"
txt += tabulate(filas, headers=list(valores.keys()), tablefmt="orgtbl")

guardarEnTxt(txt)
