import re

# === Validaciones con Expresiones Regulares ===
def validar_nombre(nombre):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚÑáéíóúñ\s]{2,}", nombre)

def validar_nota(nota):
    return re.fullmatch(r"(10|[0-9])", nota)

def validar_email(email):
    return re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email)

def validar_fecha(fecha):
    return re.fullmatch(r"\d{2}/\d{2}/\d{4}", fecha)

def clasificar_calificacion(nota):
    nota = float(nota)
    if nota < 4:
        return "Desaprobado"
    elif 4 <= nota <= 7:
        return "Aprobado"
    elif 8 <= nota <= 10:
        return "Promociona"

# Cambiar el formato de la persona para reflejar los cambios
def crear_persona(nombre, nota, dni_alumno, dni_profesor, profesor, legajo_alumno, legajo_profesor, gmail_alumno, gmail_profesor, fecha_eval, id_, instancia, materia):
    # Asegúrate de que metadatos tenga 10 elementos, incluyendo todos los campos.
    return (nombre, [nota], dni_alumno, dni_profesor, profesor, (id_, instancia, materia, dni_alumno, dni_profesor, legajo_alumno, legajo_profesor, gmail_alumno, gmail_profesor, fecha_eval))


def agregar_persona(alumnos, notas_dnis, profesores, metadatos):
    nombre = input("Nombre del alumno (o 'salir' para volver): ")
    if nombre.lower() == "salir":
        return False
    elif not validar_nombre(nombre):
        print("Nombre inválido.")
        return True

    nota = input("Nota (0-10): ")
    while not validar_nota(nota):
        print("Nota inválida. Debe ser un número entre 0 y 10.")
        nota = input("Nota (0-10): ")

    profesor = input("Profesor a cargo: ")
    while not validar_nombre(profesor):
        print("Nombre de profesor inválido.")
        profesor = input("Profesor a cargo: ")

    dni_alumno = input("DNI del alumno: ")
    dni_profesor = input("DNI del profesor: ")

    legajo_alumno = input("Legajo del alumno: ")
    legajo_profesor = input("Legajo del profesor: ")

    gmail_alumno = input("Gmail del alumno: ")
    while not validar_email(gmail_alumno):
        print("Gmail inválido.")
        gmail_alumno = input("Gmail del alumno: ")

    gmail_profesor = input("Gmail del profesor: ")
    while not validar_email(gmail_profesor):
        print("Gmail inválido.")
        gmail_profesor = input("Gmail del profesor: ")

    fecha_eval = input("Fecha de evaluación (dd/mm/aaaa): ")
    while not validar_fecha(fecha_eval):
        print("Fecha inválida. Debe ser en formato dd/mm/aaaa.")
        fecha_eval = input("Fecha de evaluación (dd/mm/aaaa): ")

    id_ = input("ID del alumno: ")
    instancia = input("Instancia (Final/Recuperatorio/etc.): ")
    materia = input("Materia: ")

    persona = crear_persona(nombre, nota, dni_alumno, dni_profesor, profesor, legajo_alumno, legajo_profesor, gmail_alumno, gmail_profesor, fecha_eval, id_, instancia, materia)

    alumnos.append(persona[0])
    notas_dnis.append(persona[1])
    profesores.append(persona[2])
    metadatos.append(persona[5])

    clasificar = lambda nota: "Desaprobado" if float(nota) < 4 else ("Aprobado" if float(nota) <= 7 else "Promociona")
    print(f"Estado de la nota: {clasificar(nota)}")


    return True

def imprimir_matriz(alumnos, notas_dnis, profesores, metadatos, titulo="Matriz de datos"):
    print(f"\n{titulo.center(250, '=')}")

    if not alumnos:
        print("(vacía)")
        return

    # Columnas con menos espacio entre ellas
    columnas = {
        "Índice": 10,
        "Alumno": 20,
        "Nota": 7,
        "Profesor": 20,
        "ID": 7,
        "Instancia": 12,
        "Materia": 15,
        "DNI Alumno": 15,
        "DNI Profesor": 15,
        "Legajo Alumno": 15,
        "Legajo Profesor": 15,
        "Gmail Alumno": 30,
        "Gmail Profesor": 30,
        "Fecha Evaluación": 15
    }

    nombres_columnas = list(columnas.keys())
    encabezado = ''.join([nombre.center(columnas[nombre]) for nombre in nombres_columnas])
    print(encabezado)
    print("=" * len(encabezado))

    for i in range(len(alumnos)):
        nota = notas_dnis[i][0]
        
        # Desempaquetamos metadatos
        id_, instancia, materia, dni_alumno, dni_profesor, legajo_alumno, legajo_profesor, gmail_alumno, gmail_profesor, fecha_eval = metadatos[i]
        
        # Profesor está en otra lista o variable
        profesor = profesores[i]  # Aquí se toma de la lista de profesores.

        # Generamos la fila de datos para cada persona
        datos = [
            str(i), alumnos[i], nota, profesor, id_, instancia,
            materia, dni_alumno, dni_profesor, legajo_alumno, legajo_profesor,
            gmail_alumno, gmail_profesor, fecha_eval
        ]

        # Imprimimos cada fila de manera alineada según los tamaños de las columnas
        fila = ''.join([str(dato).center(columnas[nombre]) for dato, nombre in zip(datos, nombres_columnas)])
        print(fila)
        print()

def modificar_dato(alumnos, notas_dnis, profesores, metadatos):
    if not alumnos:
        print("No hay datos para modificar.")
        return

    imprimir_matriz(alumnos, notas_dnis, profesores, metadatos, "Modificar datos")
    indice = input("Índice a modificar: ")
    if not indice.isdigit():
        print("Índice inválido.")
        return
    i = int(indice)
    if not (0 <= i < len(alumnos)):
        print("Índice fuera de rango.")
        return

    print("1. Alumno\n2. Nota\n3. Profesor\n4. DNI Alumno\n5. DNI Profesor\n6. ID\n7. Instancia\n8. Materia\n9. Legajo Alumno\n10. Legajo Profesor\n11. Gmail Alumno\n12. Gmail Profesor\n13. Fecha Evaluación")
    op = input("Opción (1/2/3/.../13): ")

    if op == "1":
        nuevo = input("Nuevo nombre del alumno: ")
        if validar_nombre(nuevo):
            alumnos[i] = nuevo
        else:
            print("Nombre inválido.")
    elif op == "2":
        nuevo = input("Nueva nota: ")
        while not validar_nota(nuevo):
            print("Nota inválida.")
            nuevo = input("Nueva nota: ")
        notas_dnis[i][0] = nuevo
    elif op == "3":
        nuevo = input("Nuevo profesor: ")
        if validar_nombre(nuevo):
            profesores[i] = nuevo
        else:
            print("Nombre inválido.")
    elif op == "4":
        nuevo = input("Nuevo DNI del alumno: ")
        metadatos[i][2] = nuevo
    elif op == "5":
        nuevo = input("Nuevo DNI del profesor: ")
        metadatos[i][3] = nuevo
    elif op == "6":
        metadatos[i][0] = input("Nuevo ID: ")
    elif op == "7":
        metadatos[i][1] = input("Nueva instancia: ")
    elif op == "8":
        metadatos[i][2] = input("Nueva materia: ")
    elif op == "9":
        metadatos[i][4] = input("Nuevo legajo del alumno: ")
    elif op == "10":
        metadatos[i][5] = input("Nuevo legajo del profesor: ")
    elif op == "11":
        nuevo = input("Nuevo Gmail del alumno: ")
        if validar_email(nuevo):
            metadatos[i][6] = nuevo
        else:
            print("Gmail inválido.")
    elif op == "12":
        nuevo = input("Nuevo Gmail del profesor: ")
        if validar_email(nuevo):
            metadatos[i][7] = nuevo
        else:
            print("Gmail inválido.")
    elif op == "13":
        nuevo = input("Nueva fecha de evaluación (dd/mm/aaaa): ")
        if validar_fecha(nuevo):
            metadatos[i][8] = nuevo
        else:
            print("Fecha inválida.")
    else:
        print("Opción inválida.")

def eliminar_matriz(alumnos, notas_dnis, profesores, metadatos):
    imprimir_matriz(alumnos, notas_dnis, profesores, metadatos, "Contenido antes de eliminar")
    if input("¿Eliminar la matriz? (si/no): ").lower() == "si":
        alumnos.clear()
        notas_dnis.clear()
        profesores.clear()
        metadatos.clear()
        print("Matriz eliminada.")
    else:
        print("Matriz no eliminada.")

def buscar_por_id(alumnos, notas_dnis, profesores, metadatos):
    id_buscado = input("Ingresá el ID del alumno a buscar: ")
    for i, meta in enumerate(metadatos):
        if meta[0] == id_buscado:
            imprimir_matriz([alumnos[i]], [notas_dnis[i]], [profesores[i]], [metadatos[i]], "Resultado de búsqueda")
            return
    print("ID no encontrado.")

def promedio_por_profesor(alumnos, notas_dnis, profesores):
    acumulador = {}
    for i in range(len(profesores)):
        profesor = profesores[i]
        nota = int(notas_dnis[i][0])
        if profesor not in acumulador:
            acumulador[profesor] = []
        acumulador[profesor].append(nota)

    print("\nPromedios por profesor:")
    for profesor, notas in acumulador.items():
        promedio = sum(notas) / len(notas)
        print(f"{profesor}: {promedio:.2f}")

def materias_unicas(metadatos):
    materias = set()
    for meta in metadatos:
        materias.add(meta[2]) 
    print("\nMaterias registradas (sin repetir):")
    for materia in materias:
        print(f"- {materia}")


def menu():
    alumnos = ["Lucía Martínez", "Tomás Ríos", "Valentina López", "Julián Ferreyra", "Martina Sosa"]
    notas_dnis = [["8"], ["10"], ["7"], ["9"], ["6"]]
    profesores = ["Prof. Ramírez", "Prof. Herrera", "Prof. Suárez", "Prof. Medina", "Prof. Blanco"]
    metadatos = [["ID001", "Final", "Programación", "DNI001", "DNI005", "L001", "P001", "lucia.martinez@gmail.com", "ramirez.prof@gmail.com", "10/12/2024"],
                ["ID002", "Recuperatorio", "Matemáticas", "DNI002", "DNI004", "L002", "P002", "tomas.rios@gmail.com", "herrera.prof@gmail.com", "05/12/2024"],
                ["ID003", "Final", "Base de Datos", "DNI003", "DNI003", "L003", "P003", "valentina.lopez@gmail.com", "suarez.prof@gmail.com", "15/11/2024"],
                ["ID004", "Final", "Redes", "DNI004", "DNI002", "L004", "P004", "julian.ferreyra@gmail.com", "medina.prof@gmail.com", "25/10/2024"],
                ["ID005", "Recuperatorio", "Programación", "DNI005", "DNI001", "L005", "P005", "martina.sosa@gmail.com", "blanco.prof@gmail.com", "20/09/2024"]]

    while True:
        print("\nMenu de opciones:")
        print("1. Agregar persona")
        print("2. Modificar persona")
        print("3. Buscar por ID")
        print("4. Eliminar toda la matriz")
        print("5. Ver todos los datos")
        print("6. Ver promedio por profesor")
        print("7. Salir")
        print("8. Ver materias únicas")


        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            if not agregar_persona(alumnos, notas_dnis, profesores, metadatos):
                continue
        elif opcion == "2":
            modificar_dato(alumnos, notas_dnis, profesores, metadatos)
        elif opcion == "3":
            buscar_por_id(alumnos, notas_dnis, profesores, metadatos)
        elif opcion == "4":
            eliminar_matriz(alumnos, notas_dnis, profesores, metadatos)
        elif opcion == "5":
            imprimir_matriz(alumnos, notas_dnis, profesores, metadatos, "Ver todos los datos")
        elif opcion == "6":
            promedio_por_profesor(alumnos, notas_dnis, profesores)
        elif opcion == "7":
            print("¡Hasta pronto!")
            break
        elif opcion == "8":
            materias_unicas(metadatos)
        else:
            print("Opción no válida.")

menu()