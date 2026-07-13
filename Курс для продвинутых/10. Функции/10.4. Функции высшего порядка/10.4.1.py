numbers = [4.12, 1.3257, 9.37037, 4.552, 3.186]

def map(items, func):
    new = []
    for item in items:
        new.append(func(item))
    return new

def rou(item):
    return round(item, 2)

ans = map(numbers, rou)
for a in ans:
    print(a)
