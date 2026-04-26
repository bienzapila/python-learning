set0 = [int(s) for s in input().split()]
set1 = {int(s) for s in set0}
print(len(set0) - len(set1))
