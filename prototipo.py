import re

# Validaciones con expresiones regulares
def validar_nombre(nombre):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ\s]{2,}", nombre)

def validar_nota(nota):
    return re.fullmatch(r"(10|[0-9])", nota)

def validar_tema(tema):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ0-9\s]{2,}", tema)

# Función para imprimir la matriz
imprimir_matriz = lambda m, t="Matriz de datos": (
    print(f"\n{t.center(50, '=')}") or
    (print("(vacía)") if not m else (
        print("Índice".ljust(8), "Nombre".ljust(20), "Nota".ljust(10), "Tema".ljust(20)),
        print("-" * 60),
        [print(str(i).ljust(8), m[i][0].ljust(20), str(m[i][1]).ljust(10), m[i][2].ljust(20)) for i in range(len(m))]
    ))
)

# Función para modificar un dato
def modificar_dato(m):
    imprimir_matriz(m, "Modificar datos")
    i = int(input("Ingresa el índice de la persona a modificar: "))
    if 0 <= i < len(m):
        print("\n¿Qué deseas modificar?\n1. Nombre\n2. Nota\n3. Tema")
        op = input("Elige una opción (1/2/3): ")
        if op == "1":
            nuevo = input("Nuevo nombre: ")
            if validar_nombre(nuevo):
                m[i][0] = nuevo
            else:
                print("Nombre inválido.")
        elif op == "2":
            nuevo = input("Nueva nota (0-10): ")
            if validar_nota(nuevo):
                m[i][1] = nuevo
            else:
                print("Nota inválida.")
        elif op == "3":
            nuevo = input("Nuevo tema: ")
            if validar_tema(nuevo):
                m[i][2] = nuevo
            else:
                print("Tema inválido.")
        else:
            print("Opción no válida.")
    else:
        print("Índice fuera de rango.")
    return m

# Función para eliminar la matriz
def eliminar_matriz(m):
    if input("\n¿Deseas eliminar la matriz? (si/no): ").lower() == "si":
        imprimir_matriz(m, "Contenido antes de eliminar")
        m.clear()
        print("\nLa matriz ha sido eliminada.")
    else:
        print("\nLa matriz no fue eliminada.")
    return m

# === Flujo principal ===
matriz_datos = []
while input("\n¿Deseas ingresar una persona? (si/no): ").lower() == "si":
    nombre = input("Nombre: ")
    while not validar_nombre(nombre):
        print("Nombre inválido. Solo letras y espacios.")
        nombre = input("Nombre: ")
    
    nota = input("Nota (0-10): ")
    while not validar_nota(nota):
        print("Nota inválida. Debe ser un número entre 0 y 10.")
        nota = input("Nota (0-10): ")
    
    tema = input("Tema: ")
    while not validar_tema(tema):
        print("Tema inválido. Solo letras, espacios y números.")
        tema = input("Tema: ")
    
    matriz_datos.append([nombre, nota, tema])

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
