def imprimir_matriz(matriz, titulo="Matriz de datos"):
    print(f"\n{titulo.center(50, '=')}")
    if not matriz:
        print("(vacía)")
        return
    print("Índice".ljust(8), "Nombre".ljust(20), "Nota".ljust(10), "Tema".ljust(20))
    print("-" * 60)
    for i, fila in enumerate(matriz):
        print(str(i).ljust(8), fila[0].ljust(20), str(fila[1]).ljust(10), fila[2].ljust(20))


def modificar_dato(matriz):
    imprimir_matriz(matriz, "Modificar datos")

    indice = int(input("Ingresa el índice de la persona a modificar: "))
    if 0 <= indice < len(matriz):
        print("\n¿Qué deseas modificar?")
        print("1. Nombre")
        print("2. Nota")
        print("3. Tema")
        opcion = input("Elige una opción (1/2/3): ")

        if opcion == "1":
            matriz[indice][0] = input("Nuevo nombre: ")
        elif opcion == "2":
            matriz[indice][1] = input("Nueva nota: ")
        elif opcion == "3":
            matriz[indice][2] = input("Nuevo tema: ")
        else:
            print("Opción no válida.")
    else:
        print("Índice fuera de rango.")
    return matriz


def eliminar_matriz(matriz):
    respuesta = input("\n¿Deseas eliminar la matriz? (si/no): ").lower()
    if respuesta == "si":
        imprimir_matriz(matriz, "Contenido antes de eliminar")
        matriz.clear()
        print("\nLa matriz ha sido eliminada.")
    else:
        print("\nLa matriz no fue eliminada.")
    return matriz


# === Flujo principal ===
matriz_datos = []
contador = 1
continuar = "si"

while continuar.lower() == "si":
    print(f"\nIngresar datos de persona {contador}")
    nombre = input("Nombre: ")
    nota = input("Nota: ")
    tema = input("Tema: ")

    matriz_datos.append([nombre, nota, tema])
    contador += 1
    continuar = input("¿Deseas ingresar otra persona? (si/no): ")

# Mostrar la matriz original
imprimir_matriz(matriz_datos, "Matriz original")

# Modificar datos
matriz_datos = modificar_dato(matriz_datos)

# Mostrar la matriz modificada
imprimir_matriz(matriz_datos, "Matriz modificada")

# Eliminar matriz
matriz_datos = eliminar_matriz(matriz_datos)

# Mostrar estado final
imprimir_matriz(matriz_datos, "Estado final de la matriz")