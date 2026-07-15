from functools import reduce
from operator import *

def evaluate(coefficients, x):
    return reduce(add, map(lambda a, x, i: a * x ** i, [int(c) for c in coefficients.split()], [x] * len(coefficients.split()), [i for i in range(len(coefficients.split()) - 1, -1, -1)]), 0)

print(evaluate(input(), int(input())))