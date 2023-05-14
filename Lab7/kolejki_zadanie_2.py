from Lab7.queue_zad1 import Queue
import random

def gra(moves):
    graczy = Queue()
    g = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    for i in g:
        graczy.enqueue(i)

    while graczy.size() > 1:
        for i in range(moves):
            graczy.enqueue(graczy.dequeue())

        licz = random.randint(0, 50)
        if licz % 5 == 0:
            graczy.dequeue()
    res = f"The winner is {graczy.dequeue()}"

    return res


moves = int(input("Proszę podać ilość ruchów: "))
print(gra(moves))

