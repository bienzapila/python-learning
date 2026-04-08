a = int(input())
b = int(input())
c = int(input())

lst = []
lst.append(-b / (2 * a))
lst.append((4 * a * c - b**2) / (4 * a))
print(tuple(lst))
