# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# Definir parámetros
start_date = "2025-01-01"
end_date = "2025-03-31"
date_range = pd.date_range(start=start_date, end=end_date, freq="H")

# Definir plantas del hospital
plantas = ["Planta Baja", "Primera Planta", "Segunda Planta"]

# Función para simular ocupación con variaciones diarias y semanales
def generar_ocupacion(fecha, hora, planta):
    base_ocupacion = {"Planta Baja": 10, "Primera Planta": 5, "Segunda Planta": 7}
    variabilidad = np.random.randint(-3, 4)  # Variación aleatoria
    
    # Aumentar ocupación en horario laboral (8:00 - 18:00)
    if 8 <= hora < 18:
        variabilidad += np.random.randint(5, 15)
    
    # Diferencias entre días laborables y fines de semana
    if fecha.weekday() >= 5:  # Sábado y domingo
        variabilidad -= np.random.randint(2, 6)
    
    return max(0, base_ocupacion[planta] + variabilidad)

# Generar datos
data = []
for dt in date_range:
    for planta in plantas:
        ocupacion = generar_ocupacion(dt, dt.hour, planta)
        data.append([dt.date(), dt.hour, planta, ocupacion])

# Crear DataFrame
df = pd.DataFrame(data, columns=["Fecha", "Hora", "Planta", "Ocupación"])

# Guardar en un archivo CSV
#df.to_csv("ocupacion_hospital.csv", index=False)

# Mostrar las primeras filas
print(df.head())