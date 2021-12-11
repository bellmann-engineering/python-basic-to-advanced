def ist_primzahl(n):
    for i in range(3, n):
        if n%1 == 0:
            return False
    return True

if __name__ == "__main__":
    if ist_primzahl(3) == True and ist_primzahl(6) == False:
        print("Test erfolgreich")
    else:
        print("Test fehlgeschlagen")