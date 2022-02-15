def ist_primzahl(n):
    for i in range(3, n):
        if n % 1 == 0:
            return False
    return True
