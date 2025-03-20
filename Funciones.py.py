# Función para crear la matriz de contactos
def crear_matriz():
    # Crear una matriz vacía (lista de listas)
    matriz = []
    return matriz

# Función para cargar la matriz con datos de contactos
def cargar_datos(matriz):
    # Datos de prueba (ID, Nombre, Teléfono, Email, Dirección)
    datos = [
        [1, "Juan Pérez", "555-1234", "juan.perez@email.com", "Calle Ficticia 123"],
        [2, "Ana García", "555-5678", "ana.garcia@email.com", "Av. Libertad 456"],
        [3, "Luis Martínez", "555-8765", "luis.martinez@email.com", "Calle Real 789"],
        [4, "Carla López", "555-4321", "carla.lopez@email.com", "Blvd. de la Paz 101"],
        [5, "Pedro Díaz", "555-6789", "pedro.diaz@email.com", "Calle Sol 999"]
    ]
    
    # Agregar los datos a la matriz
    for contacto in datos:
        matriz.append(contacto)

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    # Imprimir encabezados
    print(f"{'ID':<5} {'Nombre':<15} {'Teléfono':<12} {'Email':<25} {'Dirección':<20}")
    print("-" * 77)
    
    # Imprimir los datos de la matriz
    for contacto in matriz:
        print(f"{contacto[0]:<5} {contacto[1]:<15} {contacto[2]:<12} {contacto[3]:<25} {contacto[4]:<20}")

# Crear la matriz
matriz_contactos = crear_matriz()

# Cargar la matriz con los datos
cargar_datos(matriz_contactos)

# Imprimir la matriz
imprimir_matriz(matriz_contactos)
