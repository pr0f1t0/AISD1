import random
def bin_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = round((low + high)/2)
        item_guess = list[mid]
        if item_guess == item:
            return mid
        elif item_guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


size = int(input("Proszę podać rozmiar listy: "))
list = [random.randint(0, 50) for i in range(size)]
list.sort()
item = int(input("Proszę podać element poszukiwany: "))
res = bin_search(list, item)
if res != None:
    print(f"Indeks elementu poszukiwanego w liście: {res}")
else:
    print("Element nie występuje w liście")




