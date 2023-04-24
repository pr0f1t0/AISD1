import random
n = int(input("Podaj n: "))
A = [random.randint(0, 20) for i in range(n)]
print(A)
i = 0
index = "pusty"
il = 0
while i < n:
    if A[i] == 3:
        il += 1
        if index == "pusty":
            index = i
        i += 1
    else:
        i += 1
print(f'Liczba wystąpień: {il}, pierwsze wystąpienie: {index}')