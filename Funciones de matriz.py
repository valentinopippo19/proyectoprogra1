import random

def crear_matriz(filas, columnas, rango_min, rango_max):
    return [[random.randint(rango_min, rango_max) for i in range(columnas)] for i in range(filas)]

def operar_matrices(m1, m2, op):
    return [[m1[i][j] + (m2[i][j] if op == 'sumar' else -m2[i][j]) for j in range(len(m1[0]))] for i in range(len(m1))]

def multiplicar_por_escalar(matriz, escalar):
    return [[e * escalar for e in fila] for fila in matriz]

def transponer_matriz(matriz):
    return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]

def totales_y_promedios(matriz):
    filas_totales, columnas_totales = [], [0] * len(matriz[0])
    for fila in matriz:
        total_fila = 0
        for valor in fila: total_fila += valor
        filas_totales.append(total_fila)
        for j in range(len(fila)): columnas_totales[j] += fila[j]
    return filas_totales, [total / len(matriz[0]) for total in filas_totales], columnas_totales, [total / len(matriz) for total in columnas_totales]


def sumar_todos_elementos_y_promedio(matriz):
    total, elementos = 0, len(matriz) * len(matriz[0])
    for fila in matriz:
        for e in fila:
            total += e
    return total, total / elementos if elementos else 0

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Parámetros y matrices
filas, columnas, rango_min, rango_max, escalar = 5, 4, 1, 100, 3
matriz1, matriz2 = crear_matriz(filas, columnas, rango_min, rango_max), crear_matriz(filas, columnas, rango_min, rango_max)

# Operaciones e impresión
print("\nMatriz 1:"); imprimir_matriz(matriz1)
print("\nMatriz 2:"); imprimir_matriz(matriz2)
print("\nMatriz Suma:"); imprimir_matriz(operar_matrices(matriz1, matriz2, 'sumar'))
print("\nMatriz Resta:"); imprimir_matriz(operar_matrices(matriz1, matriz2, 'restar'))
print(f"\nMatriz 1 multiplicada por {escalar}:"); imprimir_matriz(multiplicar_por_escalar(matriz1, escalar))
print("\nMatriz 1 Transpuesta:"); imprimir_matriz(transponer_matriz(matriz1))

# Totales y promedios
filas_tot, filas_prom, col_tot, col_prom = totales_y_promedios(matriz1)
print("\nTotales por fila:", filas_tot)
print("Promedios por fila:", filas_prom)
print("Totales por columna:", col_tot)
print("Promedios por columna:", col_prom)

# Suma total y promedio
total, promedio = sumar_todos_elementos_y_promedio(matriz1)
print(f"\nSuma total: {total}")
print(f"Promedio: {promedio}")