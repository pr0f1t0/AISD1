def silnia(n):
    if n == 0:
        return 1
    else:
        wynik = n * silnia(n-1)
        return wynik
n = int(input("Podaj n: "))
print(silnia(n))