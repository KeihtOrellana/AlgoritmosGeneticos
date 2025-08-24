from utilidades import entero_randomico
from utilidades import real_randomico
from typing import List, Tuple
import random

def inicializar_poblacion(tamano_poblacion, N):
    poblacion = []
    for i in range(tamano_poblacion):
        individuo = crear_individuo_aleatorio(N)
        poblacion.append(individuo)
    return poblacion


def crear_individuo_aleatorio(N):
    individuo = [0] * N
    for i in range(N):
        individuo[i] = entero_randomico(N)
    return individuo


def fitness_reinas_seguras(individuo: List[int]) -> int:
    """Devuelve cuántas reinas NO son atacadas por ninguna otra (máximo = n)."""
    n = len(individuo)
    seguras = 0
    for i in range(n):
        col_i = individuo[i]
        atacada = False
        for j in range(n):
            if i == j:
                continue
            col_j = individuo[j]
            # mismo columna
            if col_i == col_j:
                atacada = True
                break
            # misma diagonal
            if abs(col_i - col_j) == abs(i - j):
                atacada = True
                break
        if not atacada:
            seguras += 1
    return seguras


def seleccion_ruleta(poblacion: List[List[int]], fitnesses: List[int]) -> List[int]:
    """Selecciona un individuo proporcionalmente a su fitness (ruleta)."""
    total = sum(fitnesses)
    if total <= 0:
        # Si todos valen 0, seleccionar uniforme al azar
        return poblacion[random.randrange(len(poblacion))][:]
    pick = real_randomico() * total
    acumulado = 0.0
    for ind, fit in zip(poblacion, fitnesses):
        acumulado += fit
        if acumulado >= pick:
            return ind[:]
    # Por estabilidad numérica
    return poblacion[-1][:]
