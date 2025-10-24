# Autores: Dennis Zavala & Jetro López - 
# Fecha: 2025-04-05
# Descripción: Modelo AR-01 como ejemplo de determinismo estocástico
# Este modelo muestra cómo un proceso aparentemente aleatorio
# puede ser descrito mediante una relación determinística con ruido aditivo.

import numpy as np
import matplotlib.pyplot as plt

# Parámetro del modelo autoregresivo AR-01
phi = 0.8       # Coeficiente autorregresivo
sigma = 1.0     # Desviación estándar del ruido
T = 100         # Número de periodos

# Generar datos usando el modelo AR-01
def generar_ar1(phi, sigma, T):
    """
    Genera una serie temporal AR-01 con coeficiente phi y ruido normal de desv. sigma.
    
    Parámetros:
        phi (float): Coeficiente autorregresivo
        sigma (float): Desviación del ruido
        T (int): Longitud de la serie
        
    Retorna:
        np.array: Serie temporal generada
    """
    X = np.zeros(T)
    epsilon = np.random.normal(0, sigma, size=T)
    for t in range(1, T):
        X[t] = phi * X[t-1] + epsilon[t]
    return X

# Generar la serie
serie = generar_ar1(phi, sigma, T)

# Graficar la serie
plt.figure(figsize=(10, 4))
plt.plot(serie, label=f'AR-01 con φ={phi}', color='blue')
plt.title("Serie Temporal AR-01 - Ejemplo de Determinismo Estocástico")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)
plt.show()

# Firma final

print("Ing. Jetro Ramón López Hernández.")

