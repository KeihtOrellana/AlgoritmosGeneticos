# Problema de las N-Reinas

El problema de las **N-Reinas** consiste en ubicar **N reinas** en un tablero de ajedrez de tamaño **N × N** de forma tal que **ninguna de ellas ataque a otra**.  
Una reina ataca en la misma fila, columna o diagonal, por lo que la solución debe garantizar que cada reina ocupe una posición segura.

Este problema pertenece a la clase de **problemas de optimización combinatoria** y es considerado **NP-completo**. Resolverlo de manera exacta implica un **crecimiento exponencial** en el número de posibilidades a medida que aumenta N. Por esta razón, se hace necesario aplicar **metaheurísticas**, que son algoritmos de búsqueda aproximada inspirados en procesos naturales.

En este trabajo se seleccionó la metaheurística de **algoritmos genéticos (AG)**, inspirada en la evolución biológica.  
El AG mantiene una **población de soluciones candidatas** que evoluciona generación tras generación mediante operadores de **selección, cruce y mutación**, con el objetivo de **maximizar una función de aptitud (fitness)**.
