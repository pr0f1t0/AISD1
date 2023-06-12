def insert_number_sort(list, number):
    i = 0
    while i < len(list) and list[i] < number:
        i += 1

    list.insert(i, number)
    return list


a = [1, 3, 4, 5, 10, 15]
print(insert_number_sort(a, 6))


