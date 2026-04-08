from math import floor, ceil


def math_round_to_int(num):
    return floor(num + 0.5) if num >= 0 else ceil(num - 0.5)


math_round_to_int(10.56)
