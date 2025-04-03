#Matriz orden

datos = [
    [1, "Juan Pérez", "555-1234", "juan.perez@email.com", "Calle Ficticia 123"],
    [2, "Ana García", "555-5678", "ana.garcia@email.com", "Av. Libertad 456"],
    [3, "Luis Martínez", "555-8765", "luis.martinez@email.com", "Calle Real 789"],
    [4, "Carla López", "555-4321", "carla.lopez@email.com", "Blvd. de la Paz 101"],
    [5, "Pedro Díaz", "555-6789", "pedro.diaz@email.com", "Calle Sol 999"]
]

def mostrar_matriz(matriz):
    encabezados = ["ID", "Nombre", "Teléfono", "Correo", "Dirección"]
    print("\n", encabezados[0], "|", encabezados[1], "|", encabezados[2], "|", encabezados[3], "|", encabezados[4])
    print("-" * 80)
    for fila in matriz:
        print(fila[0], "|", fila[1], "|", fila[2], "|", fila[3], "|", fila[4])

def ordenar_matriz(matriz, columna):
    n = len(matriz)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if matriz[j][columna] > matriz[j + 1][columna]:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
    return matriz

columna = -1
while columna < 0 or columna > 4:
    entrada = input("Ingrese el número de columna (0-4) para ordenar: ")
    if entrada.isnumeric():
        columna = int(entrada)
        if columna < 0 or columna > 4:
            print("Número de columna fuera de rango. Intente nuevamente.")
    else:
        print("Entrada no válida. Ingrese un número entero entre 0 y 4.")

matriz_ordenada = ordenar_matriz(datos, columna)
mostrar_matriz(matriz_ordenada)