import re

# === Funciones de validación con expresiones regulares ===
def validar_nombre(nombre):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ\s]{2,}", nombre)

def validar_nota(nota):
    return re.fullmatch(r"(10|[0-9])", nota)

def validar_tema(tema):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ0-9\s]{2,}", tema)

# === Función para imprimir la matriz ===
def imprimir_matriz(m, t="Matriz de datos"):
    print(f"\n{t.center(50, '=')}")
    if not m:
        print("(vacía)")
        return
    print("Índice".ljust(8), "Nombre".ljust(20), "Nota".ljust(10), "Tema".ljust(20))
    print("-" * 60)
    for i in range(len(m)):
        print(str(i).ljust(8), m[i][0].ljust(20), str(m[i][1]).ljust(10), m[i][2].ljust(20))

# === Función para pedir índice válido sin try/except ===
def pedir_indice(m):
    if not m: return None
    entrada = input("Ingresa el índice de la persona: ")
    if entrada.isdigit():
        i = int(entrada)
        if 0 <= i < len(m):
            return i
        else:
            print("Índice fuera de rango.")
    else:
        print("Índice inválido.")
    return None

# === Función para modificar un dato con validación ===
def modificar_dato(m):
    if not m: return m
    imprimir_matriz(m, "Modificar datos")
    i = pedir_indice(m)
    if i is not None:
        opciones = ["Nombre", "Nota", "Tema"]
        for j in range(len(opciones)):
            print(f"{j+1}. {opciones[j]}")
        eleccion = input("Elige una opción (1/2/3): ")
        if eleccion in ["1", "2", "3"]:
            campo = int(eleccion) - 1
            nuevo = input(f"Nuevo {opciones[campo]}: ")

            if campo == 0 and validar_nombre(nuevo):
                m[i][campo] = nuevo
            elif campo == 1 and validar_nota(nuevo):
                m[i][campo] = nuevo
            elif campo == 2 and validar_tema(nuevo):
                m[i][campo] = nuevo
            else:
                print(f"{opciones[campo]} inválido.")
        else:
            print("Opción no válida.")
    return m

# === Función para eliminar la matriz ===
def eliminar_matriz(m):
    if not m: return m
    r = input("¿Deseas eliminar la matriz? (si/no): ")
    if r == "si":
        imprimir_matriz(m, "Contenido antes de eliminar")
        m.clear()
        print("La matriz ha sido eliminada.")
    else:
        print("La matriz no fue eliminada.")
    return m

# === Menú principal sin break ===
def menu():
    matriz = []
    salir = False
    while not salir:
        print("\n" + "=" * 50)
        print("1. Ingresar nueva persona")
        print("2. Ver matriz")
        print("3. Modificar dato")
        print("4. Eliminar matriz")
        print("5. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            continuar = "si"
            while continuar == "si":
                nombre = input("Nombre (o 'salir' para cancelar): ")
                if nombre == "salir":
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

                    matriz.append([nombre, nota, tema])
                    continuar = input("¿Ingresar otra persona? (si/no): ")
        elif opcion == "2":
            imprimir_matriz(matriz)
        elif opcion == "3":
            modificar_dato(matriz)
        elif opcion == "4":
            eliminar_matriz(matriz)
        elif opcion == "5":
            print("¡Hasta luego!")
            salir = True
        else:
            print("Opción inválida.")

menu()
