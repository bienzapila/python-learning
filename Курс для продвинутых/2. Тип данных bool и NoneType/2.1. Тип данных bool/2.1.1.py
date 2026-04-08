def func(num1, num2):
    return not num1 % num2


a, b = int(input()), int(input())
if func(a, b):
    print("делится")
else:
    print("не делится")
