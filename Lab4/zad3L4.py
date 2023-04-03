import random
num = int(input("Podaj ilość liczb: "))
wektor = [random.randint(-10, 20) for i in range(num)]
print(wektor)


def maximum(l, p, A):
    if l == p:
        return A[p]
    elif (l + 1) == p:
        return max(A[l], A[p])
    else:
        mid = (l+p) // 2
        max1 = maximum(l, mid, A)
        max2 = maximum(mid, p, A)
        return max(max1, max2)


print(maximum(0, num - 1, wektor))