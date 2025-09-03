# Genetico.py
from typing import List, Tuple
import argparse, sys, random
from utilidades import set_semilla
from Nreinas import (
    inicializar_poblacion,
    evaluar_poblacion,
    seleccion_ruleta,
    cruzar_un_punto,
    mutar_reset,
    reducir_poblacion,
    es_solucion,
    imprimir_tablero,
    fitness_reinas_seguras
)

def algoritmo_genetico_n_reinas(
    N: int,
    tamano_poblacion: int,
    prob_cruza: float,
    prob_mut: float,
    iteraciones: int
) -> Tuple[List[int] | None, int]:
    """
    GA generacional con reducción por truncamiento elitista.
    - Genera hijos por cruza 1 punto
    - Aplica mutación
    - Combina padres + hijos y reduce
    - Devuelve (solución, iteración_encontrada) o (None, iteraciones)
    """
    poblacion = inicializar_poblacion(tamano_poblacion, N)

    for it in range(1, iteraciones + 1):
        fitnesses = evaluar_poblacion(poblacion)

        if it % 100 == 0:
            best = max(fitnesses)
            avg = sum(fitnesses) / len(fitnesses)
            print(f"[it {it}] best={best}  avg={avg}")

        # ¿solución exacta?
        for ind, fit in zip(poblacion, fitnesses):
            if fit == N:
                return ind[:], it

        # ---- generar hijos (misma cantidad que población) ----
        hijos: List[List[int]] = []
        while len(hijos) < tamano_poblacion:
            padre = seleccion_ruleta(poblacion, fitnesses)
            madre = seleccion_ruleta(poblacion, fitnesses)

            if random.random() < prob_cruza:
                h1, h2 = cruzar_un_punto(padre, madre)
            else:
                h1, h2 = padre[:], madre[:]

            # Mutación
            mutar_reset(h1, N, prob_mut)
            mutar_reset(h2, N, prob_mut)

            hijos.append(h1)
            if len(hijos) < tamano_poblacion:
                hijos.append(h2)

        # ---- unir padres + hijos y REDUCIR (elitismo por fitness) ----
        poblacion = reducir_poblacion(poblacion + hijos, tamano_poblacion)

    return None, iteraciones

if __name__ == "__main__":
    import random
    parser = argparse.ArgumentParser(description="N-Reinas con Algoritmo Genético")
    parser.add_argument("--semilla", type=int, default=None, help="Valor de la semilla")
    parser.add_argument("--N", type=int, default=8, help="Tamaño del tablero (N)")
    parser.add_argument("--poblacion", type=int, default=250, help="Tamaño de población")
    parser.add_argument("--pcruza", type=float, default=0.9, help="Probabilidad de cruza")
    parser.add_argument("--pmut", type=float, default=0.2, help="Probabilidad de mutación")
    parser.add_argument("--iter", type=int, default=5000, help="Número de iteraciones")
    args = parser.parse_args()

    # Semilla
    set_semilla(args.semilla)

    # Ejecutar GA
    solucion, t = algoritmo_genetico_n_reinas(
        N=args.N,
        tamano_poblacion=args.poblacion,
        prob_cruza=args.pcruza,
        prob_mut=args.pmut,
        iteraciones=args.iter
    )

    # Interfaz simple (presentación + manejo básico de errores)
    print(f"Parámetros: N={args.N}, Población={args.poblacion}, pc={args.pcruza}, pm={args.pmut}, iter={args.iter}, semilla={args.semilla}")
    if solucion is not None:
        print(f"\n¡Solución encontrada en iteración {t}!  Fitness={fitness_reinas_seguras(solucion)}/{args.N}")
        print("Individuo (fila -> columna):", solucion)
        imprimir_tablero(solucion)
        sys.exit(0)
    else:
        print("\nNo se encontró solución exacta dentro del límite de iteraciones.")
        mejor = max(inicializar_poblacion(1, args.N) + [], key=fitness_reinas_seguras)  # dummy para tipado
        # Nota: ya podrías haber guardado el 'mejor' en el loop si quieres mostrarlo.
        sys.exit(1)
