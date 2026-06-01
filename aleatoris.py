"""
Tasca 4 d'APA: Generació de números aleatoris.
Nom: Sara Lario Garrido
"""

"CLASSE Aleat"

class Aleat:
    """
    Generador de números aleatoris LGC mitjançant una classe iterable.

    Atributs:
        m (int): mòdul
        a (int): multiplicador
        c (int): increment
        x (int): estat actual o llavor de la seqüència

    Exemples:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        "Inicialitza els paràmetres del generador de forma obligatòria per clau"
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        "Retorna l'iterador (el propi objecte)"
        return self

    def __next__(self):
        "Calcula i retorna el següent nombre pseudoaleatori"
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0, /):
        "Reinicia la seqüència amb una nova llavor de forma posicional"
        self.x = x0


"FUNCIÓ aleat()"

def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Funció generadora de números aleatoris LGC.

    Arguments:
        m (int): mòdul (per defecte POSIX (2**48))
        a (int): multiplicador (per defecte POSIX)
        c (int): increment (per defecte POSIX)
        x0 (int): llavor inicial

    Exemples:
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        # enviem el valor actual, i si reben un .send(), es guarda a 'rebut'
        rebut = yield x
        if rebut is not None:
            x = rebut


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)