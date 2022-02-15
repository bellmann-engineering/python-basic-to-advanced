""" Modul mit wichtigen Funktionen zur Fibonacci-Folge """

def fib(n):
    """ Iterative Fibonacci-Funktion """
    a, b = 0, 1
    # Fehler 1
    # a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    # Fehler 2
    # if n == 20:
    #     a = 42
    return a

def fiblist(n):
    """ produziert Liste der Fibbo-Zahlen """
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib

if __name__ == "__main__":
    if fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025:
        print("Test für fib-Funktion erfolgreich")
    else:
        print("fib-Funktion liefert fehlerhafte Werte")
