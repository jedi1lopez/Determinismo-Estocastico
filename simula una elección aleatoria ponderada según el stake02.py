"""
Archivo: simula una elección aleatoria ponderada según el stake.py
Autores: Dennis Zavala & Jetro López - 
Fecha: 2025-04-05
Licencia: MIT
Descripción:
Este script simula un mecanismo de elección aleatoria ponderada según el stake,
representativo del funcionamiento del algoritmo Proof of Stake (PoS) en blockchains.
"""

# Importamos la librería random para generar elecciones aleatorias
import random

# Definimos los nodos y sus respectivos stakes (participación o apuesta)
# En este ejemplo, los nodos tienen diferentes cantidades de tokens
nodos = {
    "Nodo A": 1000,  # Mayor stake, mayor probabilidad de ser elegido
    "Nodo B": 500,
    "Nodo C": 300,
    "Nodo D": 200
}

# Calculamos el total de stake para normalizar las probabilidades
total_stake = sum(nodos.values())

# Calculamos las probabilidades de cada nodo como su stake dividido entre el total
probabilidades = [stake / total_stake for stake in nodos.values()]

# Seleccionamos un nodo al azar, ponderado por su probabilidad
validador_elegido = random.choices(list(nodos.keys()), weights=probabilidades)[0]

# Imprimimos el resultado de la elección
print(f"Validador elegido: {validador_elegido}")
