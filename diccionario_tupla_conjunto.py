import re

# === Validaciones ===
def validar_nombre(nombre):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ\s]{2,}", nombre)

def validar_nota(nota):
    return re.fullmatch(r"(10|[0-9])", nota)

def validar_tema(tema):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ0-9\s]{2,}", tema)

# === Mostrar matriz combinada ===
def imprimir_matriz(alumnos):
    print(f"\n{'Matriz de datos'.center(100, '=')}")
    if not alumnos:
        print("(vacía)")
        return

    print("Índice".ljust(6), "Alumno".ljust(20), "Nota".ljust(6), "Tema".ljust(15), "Profesor".ljust(20),
          "ID".ljust(6), "Instancia".ljust(10), "Materia".ljust(15), "Calificación".ljust(12))
    print("-" * 100)
    for i, alumno in enumerate(alumnos):
        nota, tema = alumno["nota_tema"]
        id_, instancia, materia, calificacion = alumno["metadatos"]
        print(str(i).ljust(6), alumno["nombre"].ljust(20), nota.ljust(6), tema.ljust(15),
              alumno["profesor"].ljust(20), id_.ljust(6), instancia.ljust(10),
              materia.ljust(15), calificacion.ljust(12))

# === Funciones con conjuntos ===
def mostrar_temas_unicos(alumnos):
    temas = {alumno["nota_tema"][1] for alumno in alumnos}
    print("\nTemas únicos vistos:")
    for tema in temas:
        print("-", tema)

# === Funciones con diccionarios ===
def buscar_por_id(alumnos, id_buscado):
    for alumno in alumnos:
        if alumno["metadatos"][0] == id_buscado:
            return alumno
    return None

def promedio_por_profesor(alumnos):
    print("\nPromedio de notas por profesor:")
    promedios = {}
    for alumno in alumnos:
        profe = alumno["profesor"]
        nota = int(alumno["nota_tema"][0])
        if profe not in promedios:
            promedios[profe] = []
        promedios[profe].append(nota)

    for profe, notas in promedios.items():
        promedio = sum(notas) / len(notas)
        print(f"{profe}: {promedio:.2f}")

def alumnos_aprobados(alumnos):
    print("\nAlumnos aprobados (calificación >= 4):")
    for alumno in alumnos:
        if int(alumno["metadatos"][3]) >= 4:
            print("-", alumno["nombre"])

def frecuencia_de_temas(alumnos):
    print("\nFrecuencia de cada tema:")
    temas = {}
    for alumno in alumnos:
        tema = alumno["nota_tema"][1]
        temas[tema] = temas.get(tema, 0) + 1
    for tema, cantidad in temas.items():
        print(f"{tema}: {cantidad} alumno(s)")

# === Modificar datos ===
def modificar_dato(alumnos):
    if not alumnos:
        print("No hay datos para modificar.")
        return

    imprimir_matriz(alumnos)
    indice = input("Índice a modificar: ")
    if not indice.isdigit():
        print("Índice inválido.")
        return
    i = int(indice)
    if not (0 <= i < len(alumnos)):
        print("Índice fuera de rango.")
        return

    print("1. Alumno\n2. Nota\n3. Tema\n4. Profesor\n5. ID\n6. Instancia\n7. Materia\n8. Calificación")
    op = input("Opción (1-8): ")

    if op == "1":
        nuevo = input("Nuevo nombre del alumno: ")
        if validar_nombre(nuevo):
            alumnos[i]["nombre"] = nuevo
        else:
            print("Nombre inválido.")
    elif op == "2":
        nueva = input("Nueva nota: ")
        if validar_nota(nueva):
            alumnos[i]["nota_tema"] = (nueva, alumnos[i]["nota_tema"][1])
        else:
            print("Nota inválida.")
    elif op == "3":
        nuevo = input("Nuevo tema: ")
        if validar_tema(nuevo):
            alumnos[i]["nota_tema"] = (alumnos[i]["nota_tema"][0], nuevo)
        else:
            print("Tema inválido.")
    elif op == "4":
        nuevo = input("Nuevo profesor: ")
        if validar_nombre(nuevo):
            alumnos[i]["profesor"] = nuevo
        else:
            print("Nombre inválido.")
    elif op == "5":
        nuevo = input("Nuevo ID: ")
        meta = alumnos[i]["metadatos"]
        alumnos[i]["metadatos"] = (nuevo, meta[1], meta[2], meta[3])
    elif op == "6":
        nuevo = input("Nueva instancia: ")
        meta = alumnos[i]["metadatos"]
        alumnos[i]["metadatos"] = (meta[0], nuevo, meta[2], meta[3])
    elif op == "7":
        nuevo = input("Nueva materia: ")
        meta = alumnos[i]["metadatos"]
        alumnos[i]["metadatos"] = (meta[0], meta[1], nuevo, meta[3])
    elif op == "8":
        nuevo = input("Nueva calificación: ")
        meta = alumnos[i]["metadatos"]
        alumnos[i]["metadatos"] = (meta[0], meta[1], meta[2], nuevo)
    else:
        print("Opción inválida.")

# === Eliminar todo ===
def eliminar_matriz(alumnos):
    imprimir_matriz(alumnos)
    if input("¿Eliminar la matriz? (si/no): ").lower() == "si":
        alumnos.clear()
        print("Matriz eliminada.")
    else:
        print("Matriz no eliminada.")

# === Menú principal ===
def menu():
    alumnos = [
        {
            "nombre": "Lucía Martínez",
            "nota_tema": ("8", "Funciones"),
            "profesor": "Prof. Ramírez",
            "metadatos": ("ID001", "Final", "Programación", "8")
        },
        {
            "nombre": "Tomás Ríos",
            "nota_tema": ("10", "Bucles"),
            "profesor": "Prof. Herrera",
            "metadatos": ("ID002", "Final", "Programación", "10")
        },
        {
            "nombre": "Valentina López",
            "nota_tema": ("7", "Condicionales"),
            "profesor": "Prof. Suárez",
            "metadatos": ("ID003", "Final", "Programación", "7")
        }
    ]

    salir = False
    while not salir:
        print("\n" + "=" * 70)
        print("1. Ingresar nueva persona")
        print("2. Ver matriz")
        print("3. Modificar dato")
        print("4. Eliminar matriz")
        print("5. Mostrar temas únicos")
        print("6. Buscar por ID")
        print("7. Promedio por profesor")
        print("8. Mostrar aprobados")
        print("9. Frecuencia de temas")
        print("10. Salir")
        op = input("Elegí una opción: ")

        if op == "1":
            continuar = "si"
            while continuar == "si":
                nombre = input("Nombre del alumno: ")
                if not validar_nombre(nombre):
                    print("Nombre inválido.")
                    continue

                nota = input("Nota (0-10): ")
                while not validar_nota(nota):
                    nota = input("Nota inválida. Reingrese (0-10): ")

                tema = input("Tema: ")
                while not validar_tema(tema):
                    tema = input("Tema inválido. Reingrese: ")

                profesor = input("Profesor a cargo: ")
                while not validar_nombre(profesor):
                    profesor = input("Nombre de profesor inválido. Reingrese: ")

                id_ = input("ID del alumno: ")
                instancia = input("Instancia (Final/Recuperatorio): ")
                materia = "Fundamentos de Programación"
                calificacion = input("Calificación: ")

                nuevo = {
                    "nombre": nombre,
                    "nota_tema": (nota, tema),
                    "profesor": profesor,
                    "metadatos": (id_, instancia, materia, calificacion)
                }
                alumnos.append(nuevo)
                continuar = input("¿Agregar otro alumno? (si/no): ").lower()

        elif op == "2":
            imprimir_matriz(alumnos)
        elif op == "3":
            modificar_dato(alumnos)
        elif op == "4":
            eliminar_matriz(alumnos)
        elif op == "5":
            mostrar_temas_unicos(alumnos)
        elif op == "6":
            id_buscado = input("ID a buscar: ")
            resultado = buscar_por_id(alumnos, id_buscado)
            if resultado:
                print("Alumno encontrado:")
                print(resultado)
            else:
                print("No se encontró alumno con ese ID.")
        elif op == "7":
            promedio_por_profesor(alumnos)
        elif op == "8":
            alumnos_aprobados(alumnos)
        elif op == "9":
            frecuencia_de_temas(alumnos)
        elif op == "10":
            salir = True
        else:
            print("Opción inválida.")

menu()