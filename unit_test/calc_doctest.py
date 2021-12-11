# Der doctest zu calc.py

# python -m doctest -v mein_test2.py

import doctest

def sum(a, b):
    """docstring

    >>> sum(2, 2)
    4
    >>>
    """
    return a + b

def sub(a, b):
    """docstring
    >>> sub(2, -2)
    0
    """
    return a - b

if __name__ == "__main__":
    doctest.testmod()