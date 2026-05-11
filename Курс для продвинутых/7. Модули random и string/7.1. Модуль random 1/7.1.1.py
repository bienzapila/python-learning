import random as rnd


def coin_flip():
    n = rnd.randrange(2)
    if n == 0:
        return "Орел"
    elif n == 1:
        return "Решка"
