def wspolczynnik(n, m):
    tablica = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        tablica[i][0] = 1
        tablica[i][i] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            tablica[i][j] = tablica[i-1][j] + tablica[i-1][j-1]
    return tablica[n][m]




