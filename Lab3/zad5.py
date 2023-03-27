def hanoi(krazki, pocz, pusty1, pusty2):
    if krazki >= 1:
        hanoi(krazki - 1, pocz, pusty2, pusty1)
        print(pocz, ">>", pusty1)
        hanoi(krazki - 1, pusty2, pusty1, pocz)


ilosc = int(input("Podaj ilość krążków: "))
hanoi(ilosc, "Pierwszy", "Drugi", "Trzeci")