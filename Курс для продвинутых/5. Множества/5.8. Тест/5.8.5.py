set1 = {int(c) for c in input().split()}
set2 = {int(c) for c in input().split()}
set3 = set1 & set2

if len(set3) == 0:
    print("BAD DAY")
else:
    print(*sorted(set3, reverse=True))
