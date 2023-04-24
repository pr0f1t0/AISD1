def P(row, col):
    ar = [[0 for x in range(col)] for y in range(row)]
    ar[0][0] = 0

    for j in range(1, col):
        ar[0][col] = 1

    for i in range(1, row):
        ar[row][0] = 0

    for i in range(1, row):
        for j in range(1, col):
            ar[i][j] = (ar[i - 1][j] + ar[i][j - 1]) / 2
    print(ar)

    return ar[row-1][col-1]


a = int(input("Podaj i: "))
b = int(input("Podaj j: "))
if a < 0 and b < 0:
    print("Podano złe argumenty")
else:
    print(P(a, b))





