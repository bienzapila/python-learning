numbers = [(1, 5), (0, -1, 3), (5, 7, 15)]

def comparator(number):
    return min(number) + max(number)

print(sorted(numbers, key=comparator))