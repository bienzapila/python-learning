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
    if (
        len(str(item)) == 3 and
        item % 5 == 2
    ):
        return True
    
def func(item):
    return item ** 3
    
numbers = [854, 10, 5, 452, 478, 236, 202, 41]
ans = map(filter(numbers, predicate), func)

for a in ans:
    print(a)