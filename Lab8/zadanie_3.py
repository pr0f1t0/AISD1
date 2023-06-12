def merge(lista1, lista2):
    nowa_lista = []
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            nowa_lista.append(lista1[i])
            i += 1
        else:
            nowa_lista.append(lista2[j])
            j += 1

    while i < len(lista1):
        nowa_lista.append(lista1[i])
        i += 1
    while j < len(lista2):
        nowa_lista.append(lista2[j])
        j += 1

    return nowa_lista


a = [1, 5, 7, 8, 10, 11]
b = [2, 4, 6, 9, 13]
print(merge(a, b))

