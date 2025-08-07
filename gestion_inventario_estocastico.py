"""
Archivo: gestion_inventario_estocastico.py
Autores: Dennis Zavala & Jetro López - UNESR, Venezuela
Fecha: 2025-04-05
Licencia: MIT

Descripción:
Simulación de un sistema de gestión de inventario bajo demanda estocástica.
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
D = 6000        # Demanda anual promedio (unidades)
S = 500         # Costo de pedido (Bs.)
H = 20          # Costo de mantenimiento por unidad al año (Bs.)
Z = 1.645       # Nivel de servicio del 95%
sigma_L = 100   # Desviación estándar de la demanda durante el tiempo de entrega

# Cálculo del EOQ estocástico
Q_base = np.sqrt((2 * D * S) / H)
Q_optimo = Q_base + Z * sigma_L

print(f"Cantidad óptima de pedido (Q*): {Q_optimo:.2f} unidades")

# Simulación Monte Carlo (1000 iteraciones)
np.random.seed(42)
n_simulaciones = 1000
costos_totales = []

for _ in range(n_simulaciones):
    # Simular demanda mensual (normal)
    demanda_mensual = np.random.normal(loc=500, scale=50)
    D_sim = demanda_mensual * 12  # Demanda anual simulada
    
    # Calcular pedido óptimo para esta simulación
    Q_sim = np.sqrt((2 * D_sim * S) / H) + Z * sigma_L
    
    # Calcular costos
    costo_pedido = (D_sim / Q_sim) * S
    costo_mantenimiento = (Q_sim / 2) * H
    costo_total = costo_pedido + costo_mantenimiento
    
    costos_totales.append(costo_total)

# Resultados de la simulación
costo_promedio = np.mean(costos_totales)
costo_std = np.std(costos_totales)

print(f"Costo total promedio simulado: Bs. {costo_promedio:.2f}")
print(f"Desviación estándar del costo: Bs. {costo_std:.2f}")

# Gráfico de resultados
plt.hist(costos_totales, bins=50, color='skyblue', edgecolor='black')
plt.title("Distribución del costo total (Simulación Monte Carlo)")
plt.xlabel("Costo total anual (Bs.)")
plt.ylabel("Frecuencia")
plt.axvline(costo_promedio, color='red', linestyle='--', label=f'Media: Bs. {costo_promedio:.2f}')
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()

