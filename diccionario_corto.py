import re

def validar(texto, tipo):
    patrones = {
        "nombre": r"[A-Za-zÁÉÍÓÚÑáéíóúñ\s]{2,}",
        "nota": r"(10|[0-9])",
        "tema": r"[A-Za-zÁÉÍÓÚÑáéíóúñ0-9\s]{2,}"
    }
    return re.fullmatch(patrones[tipo], texto)

def mostrar(alumnos):
    if not alumnos:
        print("No hay alumnos.")
    else:
        for id, d in alumnos.items():
            print(f"{id}: {d['nombre']} - Nota: {d['nota']} - Tema: {d['tema']} - Profesor: {d['profesor']}")

def menu():
    alumnos = {
        "ID001": {"nombre": "Lucía", "nota": "8", "tema": "Funciones", "profesor": "Ramírez"},
        "ID002": {"nombre": "Tomás", "nota": "10", "tema": "Bucles", "profesor": "Herrera"}
    }

    salir = False
    while not salir:
        op = input("\n1.Ver\n2.Agregar\n3.Modificar\n4.Eliminar\n5.Salir\n> ")

        if op == "1":
            mostrar(alumnos)

        elif op == "2":
            id_ = input("ID: ")
            if id_ in alumnos:
                print("ID ya existe.")
            else:
                nombre = input("Nombre: ")
                nota = input("Nota: ")
                tema = input("Tema: ")
                profesor = input("Profesor: ")
                if validar(nombre, "nombre") and validar(nota, "nota") and validar(tema, "tema") and validar(profesor, "nombre"):
                    alumnos[id_] = {"nombre": nombre, "nota": nota, "tema": tema, "profesor": profesor}
                else:
                    print("Datos inválidos.")

        elif op == "3":
            id_ = input("ID a modificar: ")
            if id_ not in alumnos:
                print("No existe.")
            else:
                campo = input("Campo a cambiar (nombre/nota/tema/profesor): ")
                if campo in alumnos[id_]:
                    nuevo = input(f"Nuevo {campo}: ")
                    es_valido = (
                        (campo in ["nombre", "profesor"] and validar(nuevo, "nombre")) or
                        (campo == "nota" and validar(nuevo, "nota")) or
                        (campo == "tema" and validar(nuevo, "tema"))
                    )
                    if es_valido:
                        alumnos[id_][campo] = nuevo
                    else:
                        print("Nuevo valor inválido.")
                else:
                    print("Campo inválido.")

        elif op == "4":
            id_ = input("ID a eliminar: ")
            if id_ in alumnos:
                del alumnos[id_]
            else:
                print("No existe.")

        elif op == "5":
            salir = True
        else:
            print("Opción inválida.")

menu()
