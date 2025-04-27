import re

# === Validaciones ===
def validar_nombre(nombre):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ\s]{2,}", nombre)

def validar_nota(nota):
    return re.fullmatch(r"(10|[0-9])", nota)

def validar_tema(tema):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ0-9\s]{2,}", tema)

# === Mostrar matriz combinada ===
def imprimir_matriz(alumnos, notas_temas, profesores, metadatos, titulo="Matriz de datos"):
    print(f"\n{titulo.center(70, '=')}")
    if not alumnos:
        print("(vacía)")
        return

    print("Índice".ljust(8), "Alumno".ljust(20), "Nota".ljust(6), "Tema".ljust(20), "Profesor".ljust(20), "ID".ljust(6), "Instancia".ljust(10), "Materia".ljust(15), "Calificación".ljust(12))
    print("-" * 80)
    for i in range(len(alumnos)):
        nota, tema = notas_temas[i]
        id, instancia, materia, calificacion = metadatos[i]
        print(str(i).ljust(8), alumnos[i].ljust(20), nota.ljust(6), tema.ljust(20), profesores[i].ljust(20), id.ljust(6), instancia.ljust(10), materia.ljust(15), calificacion.ljust(12))

# === Modificar datos ===
def modificar_dato(alumnos, notas_temas, profesores, metadatos):
    if not alumnos:
        print("No hay datos para modificar.")
        return

    imprimir_matriz(alumnos, notas_temas, profesores, metadatos, "Modificar datos")
    indice = input("Índice a modificar: ")
    if not indice.isdigit():
        print("Índice inválido.")
        return
    i = int(indice)
    if not (0 <= i < len(alumnos)):
        print("Índice fuera de rango.")
        return

    print("1. Alumno\n2. Nota\n3. Tema\n4. Profesor\n5. ID\n6. Instancia\n7. Materia\n8. Calificación")
    op = input("Opción (1/2/3/4/5/6/7/8): ")

    if op == "1":
        nuevo = input("Nuevo nombre del alumno: ")
        if validar_nombre(nuevo):
            alumnos[i] = nuevo
        else:
            print("Nombre inválido.")
    elif op == "2":
        nuevo = input("Nueva nota: ")
        if validar_nota(nuevo):
            notas_temas[i][0] = nuevo
        else:
            print("Nota inválida.")
    elif op == "3":
        nuevo = input("Nuevo tema: ")
        if validar_tema(nuevo):
            notas_temas[i][1] = nuevo
        else:
            print("Tema inválido.")
    elif op == "4":
        nuevo = input("Nuevo profesor: ")
        if validar_nombre(nuevo):
            profesores[i] = nuevo
        else:
            print("Nombre de profesor inválido.")
    elif op == "5":
        nuevo = input("Nuevo ID: ")
        metadatos[i][0] = nuevo
    elif op == "6":
        nuevo = input("Nueva instancia: ")
        metadatos[i][1] = nuevo
    elif op == "7":
        nuevo = input("Nueva materia: ")
        metadatos[i][2] = nuevo
    elif op == "8":
        nuevo = input("Nueva calificación: ")
        metadatos[i][3] = nuevo
    else:
        print("Opción inválida.")

# === Eliminar todo ===
def eliminar_matriz(alumnos, notas_temas, profesores, metadatos):
    imprimir_matriz(alumnos, notas_temas, profesores, metadatos, "Contenido antes de eliminar")
    if input("¿Eliminar la matriz? (si/no): ").lower() == "si":
        alumnos.clear()
        notas_temas.clear()
        profesores.clear()
        metadatos.clear()
        print("Matriz eliminada.")
    else:
        print("Matriz no eliminada.")

# === Menú principal ===
def menu():
    # === MATRICES PRE-CREADAS ===
    alumnos = ["Lucía Martínez", "Tomás Ríos", "Valentina López", "Julián Ferreyra", "Martina Sosa"]
    notas_temas = [
        ["8", "Funciones"],
        ["10", "Bucles"],
        ["7", "Condicionales"],
        ["9", "Listas"],
        ["6", "Diccionarios"]
    ]
    profesores = ["Prof. Ramírez", "Prof. Herrera", "Prof. Suárez", "Prof. Medina", "Prof. Blanco"]
    metadatos = [
        ["ID001", "Final", "Programación", "8"],
        ["ID002", "Final", "Programación", "10"],
        ["ID003", "Final", "Programación", "7"],
        ["ID004", "Final", "Programación", "9"],
        ["ID005", "Final", "Programación", "6"]
    ]

    salir = False
    while not salir:
        print("\n" + "=" * 70)
        print("1. Ingresar nueva persona")
        print("2. Ver matriz")
        print("3. Modificar dato")
        print("4. Eliminar matriz")
        print("5. Salir")
        op = input("Elegí una opción: ")

        if op == "1":
            continuar = "si"
            while continuar == "si":
                nombre = input("Nombre del alumno (o 'salir' para volver): ")
                if nombre.lower() == "salir":
                    continuar = "no"
                elif not validar_nombre(nombre):
                    print("Nombre inválido.")
                else:
                    nota = input("Nota (0-10): ")
                    while not validar_nota(nota):
                        print("Nota inválida. Debe ser un número entre 0 y 10.")
                        nota = input("Nota (0-10): ")

                    tema = input("Tema: ")
                    while not validar_tema(tema):
                        print("Tema inválido. Solo letras, números y espacios.")
                        tema = input("Tema: ")

                    profesor = input("Profesor a cargo: ")
                    while not validar_nombre(profesor):
                        print("Nombre de profesor inválido.")
                        profesor = input("Profesor a cargo: ")

                    id_ = input("ID del alumno: ")
                    instancia = input("Instancia (Final/Recuperatorio/etc.): ")
                    materia = "Fundamentos de Programación"  # Se puede personalizar según la materia
                    calificacion = input("Calificación: ")

                    alumnos.append(nombre)
                    notas_temas.append([nota, tema])
                    profesores.append(profesor)
                    metadatos.append([id_, instancia, materia, calificacion])

                    continuar = input("¿Agregar otra persona? (si/no): ").lower()

        elif op == "2":
            imprimir_matriz(alumnos, notas_temas, profesores, metadatos)

        elif op == "3":
            modificar_dato(alumnos, notas_temas, profesores, metadatos)

        elif op == "4":
            eliminar_matriz(alumnos, notas_temas, profesores, metadatos)

        elif op == "5":
            print("¡Hasta luego!")
            salir = True
        else:
            print("Opción inválida.")

menu()
