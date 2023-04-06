from functions import saludar, decirHola, array
from constants import setDefaultData, vector, incremento
from tabulate import tabulate

# prueba de datos
a, b, nombre = setDefaultData()

# prueba de impresion de elementos cambiantes
for i in range(1, 5):
    i = b
    b += 1
dato = decirHola()
print(dato)

matriz = [["Hugo", b, dato, "da", "sd", "sdf", "sdf", "sf", "dfsd", "fdgd"],
    ["Juan", 35, "Argentino", "da", "sd", "sdf", "sdf", "sf", "dfsd", "fdgd"],
    ["Pedro", 10, "Jalisco", "da", "sd", "sdf", "sdf", "sf", "dfsd", "fdgd"]]

print(tabulate(matriz, headers=["PASO", "MC", "CL1",
      "CL2", "CL3", "CL4", "n", "ES", "#MaqEnServer", "#MaqEnCola"]))
