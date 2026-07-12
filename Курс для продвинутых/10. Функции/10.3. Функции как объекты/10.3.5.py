from math import sin

n, t = int(input()), input()
def func(n, t):
    def f1(n):
        return n ** 2
    def f2(n):
        return n ** 3
    def f3(n):
        return n ** (1/2)
    def f4(n):
        return abs(n)
    def f5(n):
        return sin(n)
    commands = {'квадрат': f1, 'куб': f2, 'корень': f3, 'модуль': f4, 'синус': f5}
    return commands[t](n)

print(func(n, t))