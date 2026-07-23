import random

def get_random_string(filename):
    file = open(filename)
    return random.choice(list(map(lambda x: x.rstrip(), file.readlines())))
    