def map(items, func):
    new = []
    for item in items:
        new.append(func(item))
    return new

def reduce(operation, items, iv):
    acc = iv
    for item in items:
        acc = operation(acc, item)
    return acc

def operation(acc, item):
    return acc + item

def func(item):
    return item ** 2

numbers = [7, 5, -4, 0, 3, -5, 6, 7, 15]

ans = reduce(operation, map(numbers, func), 0)
print(ans)