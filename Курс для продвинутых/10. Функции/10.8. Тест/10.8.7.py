numbers = [(0, 2), (1, 3, 5), (-7, -9, -1)]
print(sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True))