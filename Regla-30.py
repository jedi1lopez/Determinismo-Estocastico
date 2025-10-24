# Autores: Dennis Zavala & Jetro López - 
# Fecha: 2025-04-05
def regla_30(inicial, pasos):
    ancho = len(inicial)
    for _ in range(pasos):
        siguiente = [0] * ancho
        for i in range(ancho):
            izq = inicial[(i - 1) % ancho]
            act = inicial[i]
            der = inicial[(i + 1) % ancho]
            # Aplicamos la regla 30
            if izq == 1 and act == 1 and der == 1: siguiente[i] = 0
            elif izq == 1 and act == 1 and der == 0: siguiente[i] = 0
            elif izq == 1 and act == 0 and der == 1: siguiente[i] = 0
            elif izq == 1 and act == 0 and der == 0: siguiente[i] = 1
            elif izq == 0 and act == 1 and der == 1: siguiente[i] = 1
            elif izq == 0 and act == 1 and der == 0: siguiente[i] = 1
            elif izq == 0 and act == 0 and der == 1: siguiente[i] = 1
            elif izq == 0 and act == 0 and der == 0: siguiente[i] = 0
        print(''.join(['#' if x else ' ' for x in inicial]))
        inicial = siguiente
    return inicial

# Estado inicial: solo un 1 en el centro
ancho = 81
estado_inicial = [0]*ancho
estado_inicial[ancho//2] = 1

# Simulamos 40 pasos
regla_30(estado_inicial, 40)
