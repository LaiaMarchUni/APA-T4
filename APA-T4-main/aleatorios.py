"""
LAIA MARCH CERVANTES
Implementación de un generador de números pseudoaleatorios 
basado en el Algoritmo Lineal Congruente (LGC) siguiendo el estándar POSIX, 
utilizando tanto una clase iterable como una función generadora.
"""
import doctest

class Aleat:
    """
    Clase que implementa un generador de números aleatorios LGC como iterador.

    Atributos:
        m (int): Módulo de la fórmula (rango de generación).
        a (int): Multiplicador del algoritmo.
        c (int): Incremento del algoritmo.
        x (int): Estado actual o semilla de la secuencia.

    Métodos:
        __init__: Constructor que configura los parámetros mediante claves.
        __iter__: Retorna el objeto iterador.
        __next__: Calcula y retorna el siguiente número de la secuencia.
        __call__: Reinicia la semilla de la secuencia.

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """Inicializa los parámetros del generador por clave."""
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        """Permite que el objeto sea iterable."""
        return self

    def __next__(self):
        """Aplica la fórmula LGC para obtener el siguiente valor."""
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x_nueva):
        """Reinicia la secuencia con una nueva semilla posicional."""
        self.x = x_nueva


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora de números aleatorios LGC.

    Argumentos:
        m (int): Módulo (por defecto estándar POSIX).
        a (int): Multiplicador (por defecto estándar POSIX).
        c (int): Incremento (por defecto estándar POSIX).
        x0 (int): Semilla inicial (por defecto 1212121).

    Yields:
        int: El siguiente número pseudoaleatorio en la secuencia.

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        recibido = yield x
        if recibido is not None:
            x = recibido


if __name__ == "__main__":
    doctest.testmod(verbose=True)