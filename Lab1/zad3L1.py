N = int(input("Podaj liczbę N: "))
a = int(input("Podaj liczbę wyszukiwaną: "))
A = [int(input("Podaj liczbę: ")) for i in range(N)]
l = 0
while l < N:
    if A[l]==a:
        print("Liczba wyszukiwana występuje w liście")
        break
    else:
        l += 1
        continue
else:
    print("Liczba wyszukiwana nie występuje w liście")

