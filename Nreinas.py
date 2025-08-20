from utilidades import entero_randomico
from utilidades import real_randomico

def inicializar_poblacion(tamano_población, N):
    población = []
    for i in range(tamano_población):
        individuo = crear_individuo_aleatorio(N)
        población.append(individuo)
    return población


def crear_individuo_aleatorio(N):
    individuo = [0] * N
    for i in range(N):
        individuo[i] = entero_randomico(N)
    return individuo 