def map(items, func):
    new = []
    for item in items:
        new.append(func(item))
    return new

def filter(items, predicate):
    new = []
    for item in items:
        if predicate(item):
            new.append(item)
    return new

def predicate(item):
    return abs(item) % 7 == 0 and len(str(abs(item))) == 2

def func(item):
    return item ** 2

numbers = [14, 15, -1, 2, 0, -42, 36, 2]

print(sum(map(filter(numbers, predicate), func)))



