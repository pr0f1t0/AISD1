import random
def summ(A, n):
    if n == 0:
        return 0
    elif n == 1:
        return A[0]
    else:
        mid = n // 2
        right_part = n - mid
        left= summ(A, mid)
        right = summ(A[mid:n], right_part)
        return left + right


num = int(input("Podaj ilość liczb: "))
table = [random.randint(-10, 20) for i in range(num)]
print(table)
print(summ(table, num))