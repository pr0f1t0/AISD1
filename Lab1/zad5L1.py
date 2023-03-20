import numpy as np
import random
n = int(input("Podaj ilość liczb: "))
a = np.array([[random.randint(0,20) for i in range(n)], [random.randint(0,20) for i in range(n)]])
print(a)

for i in range(2):
    pom_min = a[i][0]
    for j in range(n):
        if a[i][j] < pom_min:
            pom_min = a[i][j]
            a[i][j] = a[i][0]
    a[i][0] = pom_min


print(a)