def nwd(a, b):
    while a != b:
        if a > b:
            a = a-b
            nwd(a, b)
        else:
            b = b - a
            nwd(a, b)
    return a


a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
nwd(a, b)
