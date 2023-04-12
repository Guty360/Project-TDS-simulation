from datetime import datetime
from tabulate import tabulate
import random

def ingresarValoresEnteros(indicacion):
    entrada = input(indicacion)
    if not entrada.isdigit():
        print("\nIngrese un numero entero valido! ")
        entrada = ingresarValoresEnteros(indicacion)
    elif int(entrada) > 1000 or int(entrada) < 0:
        print("\nIngrese un numero entero valido! (maximo: 1000, minimo: 0) ")
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

    cantidadDeClocks = ingresarValoresEnteros("Cuantas maquinas, (clocks), le gustaria ingresar? (minimo: 3, maximo 10)\n")

    if cantidadDeClocks < 3 or cantidadDeClocks > 10:
        clocks = ingresarDatosPorUsuario()
    else:
        for i in range(0, cantidadDeClocks):
            clocks.append( ingresarValoresEnteros("Ingrese el clock" + str(i) +": ") )

    return clocks


def ingresarDatosPorAletoriedad():
    clocks = []

    cantidadDeClocks = ingresarValoresEnteros("Cuantas maquinas, (clocks), le gustaria ingresar? (minimo: 3, maximo: 10)\n")

    if cantidadDeClocks < 3 or cantidadDeClocks > 10:
        print("\nChistosito, que no sabe leer?")
        clocks = ingresarDatosPorAletoriedad()
    
    for i in range(0, cantidadDeClocks):
        clocks.append(random.randint(1, 100))

    return clocks