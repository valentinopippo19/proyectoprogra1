#Factura

def pedir_datos():
    print("\n--- Generación de Factura / Ficha de Producto ---\n")
    
    nombre = input("Ingrese el nombre del producto/servicio: ")
    descripcion = input("Ingrese una descripción breve: ")
    if len(descripcion) > 50:
        descripcion = descripcion[:50] + "..."
    
    precio = input("Ingrese el precio unitario: ")
    while not ("." in precio or (precio >= "0" and precio <= "9")):
        print("Error: Ingrese un número válido para el precio.")
        precio = input("Ingrese el precio unitario: ")
    precio = float(precio)
    
    cantidad = input("Ingrese la cantidad: ")
    while not (cantidad >= "0" and cantidad <= "9"):
        print("Error: Ingrese un número entero válido para la cantidad.")
        cantidad = input("Ingrese la cantidad: ")
    cantidad = int(cantidad)
    
    disponibilidad = input("¿Está disponible? (True/False): ").strip()
    disponibilidad = "Sí" if disponibilidad in ["True", "1", "si", "sí"] else "No"
    
    return nombre, descripcion, precio, cantidad, disponibilidad

def generar_factura():
    nombre, descripcion, precio, cantidad, disponibilidad = pedir_datos()
    total = precio * cantidad
    
    reporte = f"""
    ======================================
                  FACTURA
    ======================================
    Producto/Servicio: {nombre.ljust(20)}
    Descripción      : {descripcion}
    Precio Unitario  : ${precio:>10.2f}
    Cantidad        : {cantidad:>10}
    --------------------------------------
    TOTAL          : ${total:>10.2f}
    --------------------------------------
    Disponibilidad  : {disponibilidad}
    ======================================
    """
    print(reporte)

generar_factura()
