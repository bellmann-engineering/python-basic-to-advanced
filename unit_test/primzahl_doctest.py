# python -m doctest -v primzahl_doctest.py

import doctest

def ist_primzahl(n):
    """docstring

    >>> ist_primzahl(3)
    True
    >>> ist_primzahl(6)
    False
    >>>
    """
    for i in range(3, n):
        if n%1 == 0:
            return False
    return True

if __name__ == "__main__":
    doctest.testmod()





