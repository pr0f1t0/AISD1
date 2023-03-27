def dec_to_bin(num):
    if num == 0:
        return "0"
    else:
        rem = num % 2
        res = dec_to_bin(num // 2)
        return res + str(rem)


num = int(input("Podaj liczbę: "))
print(dec_to_bin(num))
