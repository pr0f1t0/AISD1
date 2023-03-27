def nwd(a, b):
    while b != 0:
        c = b
        b = a % b
        a = c
        nwd(a, b)
    return a


a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
nwd(a, b)

