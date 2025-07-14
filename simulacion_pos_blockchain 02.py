"""
Archivo: simulacion_pos_blockchain.py
Autor: Dr. Jetro López - UNESR, Venezuela
Fecha: 2025-04-06
Licencia: MIT
Descripción:
Simula la selección de un nodo validador usando Proof of Stake (PoS)
con probabilidad proporcional al balance de cada nodo.
"""

import random

def seleccionar_nodo_validador(nodos):
    """
    Selecciona un nodo validador basado en su stake (saldo).

    Parámetros:
        nodos (dict): Diccionario con nodos y sus stakes

    Retorna:
        str: Nombre del nodo seleccionado
    """
    nombres = list(nodos.keys())
    stakes = list(nodos.values())
    total_stake = sum(stakes)  # Calculamos el total del stake
    probabilidades = [s / total_stake for s in stakes]  # Normalizamos probabilidades
    
    # Seleccionamos un nodo con probabilidad proporcional a su stake
    return random.choices(nombres, weights=probabilidades, k=1)[0]

if __name__ == '__main__':
    # Definimos los nodos y sus respectivos stakes
    nodos = {
        "Nodo_A": 100,
        "Nodo_B": 300,
        "Nodo_C": 600
    }

    # Simulamos la selección de validadores durante 5 bloques consecutivos
    for i in range(5):
        seleccionado = seleccionar_nodo_validador(nodos)
        print(f"✅ Bloque {i+1}: Nodo seleccionado → {seleccionado}")