import re

# === Validaciones con expresiones regulares ===
def validar_nombre(nombre):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ\s]{2,}", nombre)

def validar_nota(nota):
    return re.fullmatch(r"(10|[0-9])", nota)

def validar_tema(tema):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ0-9\s]{2,}", tema)

# === Función lambda para imprimir la matriz ===
imprimir_matriz = lambda m, t="Matriz de datos": (
    print(f"\n{t.center(50, '=')}") or
    (print("(vacía)") if not m else (
        print("Índice".ljust(8), "Nombre".ljust(20), "Nota".ljust(10), "Tema".ljust(20)),
        print("-" * 60),
        [print(str(i).ljust(8), *[str(e).ljust(w) for e, w in zip(m[i], [20, 10, 20])]) for i in range(len(m))]
    ))
)

# === Función para modificar un dato (con validaciones) ===
def modificar_dato(m):
    if not m: return m
    imprimir_matriz(m, "Modificar datos")

    indice = input("Índice a modificar: ")
    if not indice.isdigit(): print("Índice inválido."); return m
    i = int(indice)

    if not (0 <= i < len(m)):
        print("Índice fuera de rango.")
        return m

    campos = ["Nombre", "Nota", "Tema"]
    print("\n".join([f"{j+1}. {c}" for j, c in enumerate(campos)]))
    op = input("Opción (1/2/3): ")

    if op in ["1", "2", "3"]:
        nuevo_valor = input(f"Nuevo {campos[int(op)-1]}: ")
        campo = int(op) - 1

        if campo == 0 and validar_nombre(nuevo_valor):
            m[i][campo] = nuevo_valor
        elif campo == 1 and validar_nota(nuevo_valor):
            m[i][campo] = nuevo_valor
        elif campo == 2 and validar_tema(nuevo_valor):
            m[i][campo] = nuevo_valor
        else:
            print(f"{campos[campo]} inválido.")
    else:
        print("Opción no válida.")
    return m

# === Función lambda para eliminar la matriz ===
eliminar_matriz = lambda m: (
    (imprimir_matriz(m, "Contenido antes de eliminar") or m.clear() or print("Matriz eliminada."))
    if input("¿Eliminar la matriz? (si/no): ").lower() == "si" else print("Matriz no eliminada.")
) or m

# === Menú principal sin breaks ===
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

                    matriz.append([nombre, nota, tema])
                    continuar = input("¿Agregar otra? (si/no): ").lower()

        elif op == "2":
            imprimir_matriz(matriz)

        elif op == "3":
            modificar_dato(matriz)

        elif op == "4":
            eliminar_matriz(matriz)

        elif op == "5":
            print("¡Hasta luego!")
            salir = True

        else:
            print("Opción inválida.")

menu()

# datos cargados automaticamente en las tres, matriz de notas, alumnos y profesor tienen que ser tres por separado pero relacionadas.