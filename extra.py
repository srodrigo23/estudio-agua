import pandas as pd
import numpy as np

# Crear un DataFrame con 100000 filas y una columna de 'Consumo' con valores aleatorios entre 0 y 999
np.random.seed(0)  # Para reproducibilidad
df = pd.DataFrame({
    'Consumo': np.random.randint(0, 1000, size=100000)
})

# Definir una función para calcular el cargo basado en el consumo
def calcular_cargo(consumo):
    if consumo <= 12:
        return 20
    elif consumo <= 25:
        return 1.31 * (consumo - 12) + 20
    elif consumo <= 50:
        return 1.50 * (consumo - 25) + 20 + 1.31 * 13
    elif consumo <= 75:
        return 2.24 * (consumo - 50) + 20 + 1.31 * 13 + 1.50 * 25
    elif consumo <= 100:
        return 2.85 * (consumo - 75) + 20 + 1.31 * 13 + 1.50 * 25 + 2.24 * 25
    elif consumo <= 150:
        return 3.40 * (consumo - 100) + 20 + 1.31 * 13 + 1.50 * 25 + 2.24 * 25 + 2.85 * 25
    else:
        return 3.99 * (consumo - 150) + 20 + 1.31 * 13 + 1.50 * 25 + 2.24 * 25 + 2.85 * 25 + 3.40 * 50

# Aplicamos la función a la columna de 'Consumo' para obtener una nueva columna 'Cargo'
df['Cargo'] = df['Consumo'].apply(calcular_cargo)

print(df.head())  # Mostrar las primeras filas del DataFrame resultante


import pandas as pd

# Supongamos que tenemos un DataFrame con lecturas de un medidor de agua
df = pd.DataFrame({
    'Fecha': ['2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04'],
    'Lectura': [150, 160, 170, 180]
})

# Convertir la columna de fecha a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Definir un valor de lectura específico para filtrar
lectura_objetivo = 160

# Filtrar el DataFrame para las lecturas iguales al valor objetivo
df_filtrado = df[df['Lectura'] == lectura_objetivo]

print(df_filtrado)

# este es en el caso que querramos un rango de lecuta
df_filtrado = df[(df['Lectura'] >= 160) & (df['Lectura'] <= 170)]