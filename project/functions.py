from datetime import datetime

def ingresarValoresEnteros(indicacion):
    entrada = input(indicacion)
    if not entrada.isdigit():
        print("\nIngrese un numero entero valido! ")
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
    respuesta = input("Desea ingresar los datos? (y/n)\n")
    clocks= []
    if(respuesta == 'y' or respuesta == 'Y'):
        for i in range(0,4):
            clocks.append( ingresarValoresEnteros("Ingrese el clock" + str(i) +" :\n") )
    elif(respuesta == 'n' or respuesta == 'N'):
        clocks = [53, 5, 14, 31]
    else:
        print("\nSea serio por favor :/\n")
        clocks = cargarDatos()
    
    return clocks
