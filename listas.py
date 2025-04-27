import re

# === Validaciones con expresiones regulares ===
def validar_nombre(nombre):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ\s]{2,}", nombre)

def validar_nota(nota):
    return re.fullmatch(r"(10|[0-9])", nota)

def validar_tema(tema):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ0-9\s]{2,}", tema)

# === Función para imprimir la matriz ===
def imprimir_matriz(alumnos, notas, temas, titulo="Matriz de datos"):
    print(f"\n{titulo.center(50, '=')}")
    if not alumnos:
        print("(vacía)")
        return

    print("Índice".ljust(8), "Nombre".ljust(20), "Nota".ljust(10), "Tema".ljust(20))
    print("-" * 60)
    for i in range(len(alumnos)):
        print(str(i).ljust(8), alumnos[i].ljust(20), notas[i].ljust(10), temas[i].ljust(20))

# === Función para modificar un dato (con validaciones) ===
def modificar_dato(alumnos, notas, temas):
    if not alumnos:
        print("No hay datos para modificar.")
        return

    imprimir_matriz(alumnos, notas, temas, "Modificar datos")
    indice = input("Índice a modificar: ")
    if not indice.isdigit():
        print("Índice inválido.")
        return
    i = int(indice)
    if not (0 <= i < len(alumnos)):
        print("Índice fuera de rango.")
        return

    print("1. Nombre\n2. Nota\n3. Tema")
    op = input("Opción (1/2/3): ")

    if op == "1":
        nuevo = input("Nuevo nombre: ")
        if validar_nombre(nuevo):
            alumnos[i] = nuevo
        else:
            print("Nombre inválido.")
    elif op == "2":
        nuevo = input("Nueva nota: ")
        if validar_nota(nuevo):
            notas[i] = nuevo
        else:
            print("Nota inválida.")
    elif op == "3":
        nuevo = input("Nuevo tema: ")
        if validar_tema(nuevo):
            temas[i] = nuevo
        else:
            print("Tema inválido.")
    else:
        print("Opción inválida.")

# === Función para eliminar la matriz ===
def eliminar_matriz(alumnos, notas, temas):
    imprimir_matriz(alumnos, notas, temas, "Contenido antes de eliminar")
    if input("¿Eliminar la matriz? (si/no): ").lower() == "si":
        alumnos.clear()
        notas.clear()
        temas.clear()
        print("Matriz eliminada.")
    else:
        print("Matriz no eliminada.")

# === Menú principal ===
def menu():
    alumnos = []
    notas = []
    temas = []

    salir = False
    while not salir:
        print("\n" + "=" * 50)
        print("1. Ingresar nueva persona")
        print("2. Ver matriz")
        print("3. Modificar dato")
        print("4. Eliminar matriz")
        print("5. Salir")
        op = input("Elegí una opción: ")

        if op == "1":
            continuar = "si"
            while continuar == "si":
                nombre = input("Nombre (o 'salir' para volver): ")
                if nombre.lower() == "salir":
                    continuar = "no"
                elif not validar_nombre(nombre):
                    print("Nombre inválido. Solo letras y espacios (mínimo 2 caracteres).")
                else:
                    nota = input("Nota (0-10): ")
                    while not validar_nota(nota):
                        print("Nota inválida. Debe ser un número entre 0 y 10.")
                        nota = input("Nota (0-10): ")

                    tema = input("Tema: ")
                    while not validar_tema(tema):
                        print("Tema inválido. Solo letras, números y espacios (mínimo 2 caracteres).")
                        tema = input("Tema: ")

                    alumnos.append(nombre)
                    notas.append(nota)
                    temas.append(tema)

                    continuar = input("¿Agregar otra? (si/no): ").lower()

        elif op == "2":
            imprimir_matriz(alumnos, notas, temas)

        elif op == "3":
            modificar_dato(alumnos, notas, temas)

        elif op == "4":
            eliminar_matriz(alumnos, notas, temas)

        elif op == "5":
            print("¡Hasta luego!")
            salir = True

        else:
            print("Opción inválida.")

menu()
