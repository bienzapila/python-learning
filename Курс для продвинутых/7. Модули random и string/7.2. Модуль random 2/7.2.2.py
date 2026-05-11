from random import *
import string


def generate_index():
    return f"{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{randrange(0,100)}_{randrange(0,100)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}"


print(generate_index)
