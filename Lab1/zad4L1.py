n = int(input("Podaj liczbę n: "))
A = [int(input("Podaj liczbę: ")) for i in range(n)]
i = 0
min = A[1]
while i < n:
    if A[i] < min:
        min = i
print(min)