from operator import *

def arithmetic_operation(op):
    ops = {'+': add, '-': sub, '*': mul, '/': truediv}
    return ops[op]

