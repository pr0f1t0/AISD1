def nwd(a, b):
    while a != b:
        if a > b:
            nwd(a-b, b)
        else:
            nwd(a, b-a)
    return a

print(nwd(12, 18))