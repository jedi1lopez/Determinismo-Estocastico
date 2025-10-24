"""
Archivo: prediccion_caidas_web.py
Autores: Dennis Zavala & Jetro López -
Fecha: 2025-04-05
Licencia: MIT

Descripción:
Simulación de caídas de un servidor web usando cadenas de Markov.
"""

import numpy as np

# Matriz de transición de estados
# Estados: 0 = operativo, 1 = falla leve, 2 = caído
matriz_transicion = np.array([
    [0.8, 0.15, 0.05],
    [0.3, 0.6, 0.1],
    [0.0, 0.4, 0.6]
])

def simular_dias(num_dias):
    estado_actual = 0
    historial = [estado_actual]

    for _ in range(num_dias):
        estado_actual = np.random.choice([0, 1, 2], p=matriz_transicion[estado_actual])
        historial.append(estado_actual)

    return historial

if __name__ == '__main__':
    dias_simulados = simular_dias(30)
    print("📊 Historial de estado del sistema por 30 días:")
    print(dias_simulados)
