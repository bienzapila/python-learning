numbers = [(0, 0), (1, 1), (2, 2, 2), (3,)]

def avg(lst):
    return sum(lst)/len(lst)

print(min(numbers, key=avg))
print(max(numbers, key=avg))