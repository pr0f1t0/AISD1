import numpy as np
n = int(input("Podaj wymiar: "))
F = np.array(n,n)
print(F)
def func(i, j):
    i, j = n
    for x in range(i):
        while i == 0 and j > 0:
            F.append(1)
            i += 1
        for y in range(j):
            while j == 0 and i > 0:
                F.append(0)
                j += 1






