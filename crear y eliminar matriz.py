# Inicializar la matriz
matriz_datos = []

continuar = "si"
contador = 1

while continuar == "si":
    print("\nPersona", contador)
    nombre = input("Nombre: ")
    nota = input("Nota: ")
    tema = input("Tema: ")

    matriz_datos.append([nombre, nota, tema])
    contador += 1

    continuar = input("¿Deseas ingresar otra persona? (si/no): ")

# Imprimir la matriz como tabla con tabulaciones
print("\nMatriz de datos (Nombre | Nota | Tema):\n")
print("Nombre\t\tNota\tTema")
print("----------------------------------------")
for fila in matriz_datos:
    print(fila[0] + "\t\t" + str(fila[1]) + "\t" + fila[2])

def eliminar_matriz(matriz):
    eliminar = input("\n¿Eliminar matriz? (si/no): ")
    if eliminar.lower() == "si":
        print("\nContenido de la matriz antes de eliminarla:\n")
        print("Nombre\t\tNota\tTema")
        print("----------------------------------------")
        for fila in matriz:
            print(fila[0] + "\t\t" + str(fila[1]) + "\t" + fila[2])

        matriz.clear()  # Vacía la matriz
        print("\nLa matriz ha sido eliminada (vacía ahora).")
    else:
        print("\nLa matriz no fue eliminada.")
    return matriz

# Llamada a la función
matriz_datos = eliminar_matriz(matriz_datos)

# Mostrar matriz actual para verificar si quedó vacía o no
print("\nEstado final de la matriz:")
print("Nombre\t\tNota\tTema")
print("----------------------------------------")
if matriz_datos:
    for fila in matriz_datos:
        print(fila[0] + "\t\t" + str(fila[1]) + "\t" + fila[2])
else:
    print("(vacía)")