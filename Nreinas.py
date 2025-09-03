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

def cruzar_un_punto(padre: List[int], madre: List[int]) -> Tuple[List[int], List[int]]:
    """Cruza de 1 punto (compatible con representación libre)."""
    n = len(padre)
    if n <= 1:
        return padre[:], madre[:]
    punto = random.randint(1, n - 1)
    h1 = padre[:punto] + madre[punto:]
    h2 = madre[:punto] + padre[punto:]
    return h1, h2

def cruzar_un_punto(padre: List[int], madre: List[int]) -> Tuple[List[int], List[int]]:
    """Cruza de 1 punto (compatible con representación libre)."""
    n = len(padre)
    if n <= 1:
        return padre[:], madre[:]
    punto = random.randint(1, n - 1)
    h1 = padre[:punto] + madre[punto:]
    h2 = madre[:punto] + padre[punto:]
    return h1, h2

def mutar_reset(individuo: List[int], N: int, prob_mut: float) -> None:
    """Mutación: reasigna la columna de una fila elegida al azar."""
    if random.random() < prob_mut:
        fila = random.randrange(N)
        individuo[fila] = entero_randomico(N)  # asume [0..N-1]

def evaluar_poblacion(poblacion: List[List[int]]) -> List[int]:
    return [fitness_reinas_seguras(ind) for ind in poblacion]

def es_solucion(individuo: List[int]) -> bool:
    return fitness_reinas_seguras(individuo) == len(individuo)

def imprimir_tablero(individuo: List[int]) -> None:
    n = len(individuo)
    for r in range(n):
        fila = []
        for c in range(n):
            fila.append("Q" if individuo[r] == c else ".")
        print(" ".join(fila))
    print()

def reducir_poblacion(poblacion: List[List[int]], tamano_objetivo: int) -> List[List[int]]:
    """
    Elitismo por truncamiento: ordena por fitness desc y corta.
    """
    poblacion_ordenada = sorted(poblacion, key=fitness_reinas_seguras, reverse=True)
    return poblacion_ordenada[:tamano_objetivo]
