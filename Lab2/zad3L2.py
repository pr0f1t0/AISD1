n = int(input("Podaj ilość liczb: "))
A = [input("Podaj liczby: ") for i in range(n)]
pom = [str(i) for i in A]
pom.sort()
A = [int(i) for i in pom]
print(A)





