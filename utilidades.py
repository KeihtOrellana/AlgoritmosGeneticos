import random

#Generar un número real randóminco entre [0 y 1].
def real_randomico():
    return random.random()

#Generar un número entero randóminco entre [1 y N].
def entero_randomico(N):
    return random.randint(1,N)

def set_semilla(seed: int | None) -> None:
    if seed is not None:
        random.seed(seed)

def real_randomico() -> float:
    return random.random()

def entero_randomico(N: int) -> int:
    return random.randrange(N)