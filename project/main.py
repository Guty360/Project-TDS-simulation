from functions import guardarEnTxt, cargarDatos, matriz, textoMatriz

#! Entradas
## Datos a pedir al usuario
### Pedimos los clocks
clocks = cargarDatos()

## Datos del sistema
### Ajuste generales del sistema
ajuste = {
    "tiempoSeteoYAjuste" : 11,
    "tiempoNormalDeUsoDeMaquina" : 480,
    "cantidadDeEjecucciones" : 25
}

#* Clock del servidor
# clockServidor = max(clocks) * 10000
clockServidor = 1000000

out = [clockServidor + 1]
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



#! Proceso
## Invocamos las funcion de la tabla
matriz = matriz(valores, ajuste, clocks, out, clockServidor)



#! Salida
txt = textoMatriz(ajuste, valores, matriz)

## Imprimimos en consola los valores obtenidos
print(txt)

## Guardamos en un txt los valores obtenidos
guardarEnTxt(txt)