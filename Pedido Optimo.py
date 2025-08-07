# Autores: Dennis Zavala & Jetro López - UNESR, Venezuela
# Fecha: 2025-04-05
import numpy as np

np.random.seed(42)
def calcular_pedido_optimo(D, S, H, Z, sigma_L):
    Q_base = np.sqrt((2 * D * S) / H)
    Q_estocastico = Q_base + Z * sigma_L
    return Q_estocastico

# Parámetros
D = 6000  # Demanda anual
S = 500    # Costo de pedido
H = 20     # Costo de mantenimiento
Z = 1.645  # Nivel de servicio del 95%
sigma_L = 100  # Desviación estándar durante el tiempo de entrega

Q_optimo = calcular_pedido_optimo(D, S, H, Z, sigma_L)
print(f"Cantidad óptima de pedido: {Q_optimo:.2f} unidades")
