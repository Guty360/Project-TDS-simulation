from datetime import datetime
from tabulate import tabulate
import random
import json

def ingresarValoresEnteros(indicacion):
    entrada = input(indicacion)
    if not entrada.isdigit():
        print("\nIngrese un numero entero valido! ")
        entrada = ingresarValoresEnteros(indicacion)
    elif int(entrada) > 10000 or int(entrada) < 0:
        print("\nIngrese un numero entero valido! (maximo: 10000, minimo: 0) ")
        entrada = ingresarValoresEnteros(indicacion)
    return int(entrada)

def guardarEnTxt(texto):
    fecha_hora_actual = datetime.now()
    cadena_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%d_%H:%M:%S")
    nombre = cadena_fecha_hora + '.txt'
    archivo = open(nombre, "w")
    archivo.write(texto)
    archivo.close()

def valoresDeUnDiccionario(diccionario):
    # Crear una tupla vacía para almacenar los valores
    valores = ()

    # Iterar sobre los valores del diccionario
    for valor in diccionario.values():
        # Verificar si el valor es numérico
        if isinstance(valor, (int, float)):
            # Convertir el valor a string y agregarlo a la tupla
            valores += (str(valor),)
        else:
            # Agregar el valor a la tupla
            valores += (valor,)
    return valores


def cargarDatos():
    print("Como desea ingresar los datos los datos?\n")
    opciones = [("1", "Me gustaria usar una semilla"), ("2","Yo deseo ingresar todos los valores"), ("3", "Preferiria usar datos aleatorios")]
    print(tabulate(opciones, headers=["Numero", "Opcion"], tablefmt="orgtbl"))
    respuesta = ingresarValoresEnteros("\nIngrese el numero de la opcion que desea usar: ")
    
    clocks= []

    if respuesta == 1:
        clocks = ingresarDatosPorSemilla()
    elif respuesta == 2:
        clocks = ingresarDatosPorUsuario()
    elif respuesta == 3:
        clocks = ingresarDatosPorAletoriedad()
    else:
        print("\nSea serio por favor :/")
        cargarDatos()
    
    return clocks


def ingresarDatosPorSemilla():
    clocks = [53, 5, 14, 31]

    return clocks


def ingresarDatosPorUsuario():
    clocks = []

    cantidadDeClocks = ingresarValoresEnteros("Cuantas maquinas, (clocks), le gustaria ingresar? (minimo: 3)\n")

    if cantidadDeClocks < 3:
        clocks = ingresarDatosPorUsuario()
    else:
        for i in range(0, cantidadDeClocks):
            clocks.append( ingresarValoresEnteros("Ingrese el clock" + str(i) +": ") )

    return clocks


def ingresarDatosPorAletoriedad():
    clocks = []

    cantidadDeClocks = ingresarValoresEnteros("Cuantas maquinas, (clocks), le gustaria ingresar? (minimo: 3)\n")

    if cantidadDeClocks < 3:
        print("\nChistosito, que no sabe leer?")
        clocks = ingresarDatosPorAletoriedad()
    
    for i in range(0, cantidadDeClocks):
        clocks.append(random.randint(1, 1000))

    return clocks

def matriz(valores, ajuste, clocks, out, clockServidor):
    filas = [tuple(valores.values())]

    # Usamos un auxiliar y determinamos los outs
    clocksAuxiliar = []
    for i in range(0, len(clocks)+1):
        clocksAuxiliar.append(valores["clock{}".format(i+1)])
        out.append(out[0]+i)

    for i in range(0, ajuste["cantidadDeEjecucciones"]):    

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

        # * Obtenemos el numero de maquinas en proceso
        valores["numero"] = 0
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
            i += 1

    return filas

def textoMatriz(ajuste, valores, matriz):
    txt = "Los ajustes usados son:\n"
    txt += json.dumps(ajuste)
    txt += "\n\n"
    txt += tabulate(matriz, headers=list(valores.keys()), tablefmt="orgtbl")

    return txt