numbers = [1, 72, 2, 3, 84, 15]

print(*filter(lambda x: False if str(x) == str(x)[::-1] else True, numbers))