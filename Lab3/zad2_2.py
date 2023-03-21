a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
while b != 0:
        c = a
        a = b
        b = c % b
else:
    print(a)
