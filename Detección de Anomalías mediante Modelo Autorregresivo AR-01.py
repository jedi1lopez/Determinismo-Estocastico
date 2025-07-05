# =====================================================================
# Detección de Anomalías mediante Modelo Autorregresivo AR(1)
# Autor: Jetro Ramón López Hernández
# Institución: Universidad Nacional Experimental Simón Rodríguez (UNESR)
# Fecha: 14 de abril de 2025
# Descripción:
# Este script genera una serie temporal sintética bajo un modelo AR(1),
# simula un evento anómalo (fraude), y muestra gráficamente su detección.
# =====================================================================

# Importar librerías necesarias
import numpy as np      # Para operaciones numéricas
import matplotlib.pyplot as plt  # Para visualización gráfica

# =====================================================================
# Definición de parámetros del modelo AR(1)
# =====================================================================
T = 100         # Número total de observaciones (periodos)
phi = 0.8       # Coeficiente autorregresivo (|phi| < 1 para estabilidad)
sigma = 1.0     # Desviación estándar del ruido gaussiano

# =====================================================================
# Generación de la serie temporal AR(1)
# Y[0] = 0 es el valor inicial
# Cada valor subsiguiente depende del anterior y de un término aleatorio
# =====================================================================
Y = np.zeros(T)  # Inicializa la serie con ceros

for t in range(1, T):
    epsilon = np.random.normal(0, sigma)  # Ruido blanco gaussiano
    Y[t] = phi * Y[t - 1] + epsilon       # Ecuación del modelo AR(1)

# =====================================================================
# Simulación de un evento anómalo (fraude financiero)
# Introducimos un "fraude" en el periodo 80, añadiendo un valor atípico
# =====================================================================
Y[80] += 10  # Incremento artificial para representar un fraude o anomalía

# =====================================================================
# Visualización gráfica de la serie temporal con evento anómalo
# =====================================================================
plt.figure(figsize=(12, 5))  # Configura tamaño de gráfico

# Gráfica principal
plt.plot(Y, label='Serie Temporal AR(1)', color='blue')

# Línea vertical roja que marca el momento del evento anómalo
plt.axvline(x=80, color='red', linestyle='--', label='Evento Anómalo (Fraude Simulado)')

# Etiquetas y estilo
plt.title('Detección de Fraude usando Modelo AR(1)')
plt.xlabel('Tiempo')
plt.ylabel('Valor Observado')
plt.legend()
plt.grid(True)

# Mostrar gráfico final
plt.tight_layout()
plt.show()

# =====================================================================
# FIN DEL SCRIPT
# =====================================================================