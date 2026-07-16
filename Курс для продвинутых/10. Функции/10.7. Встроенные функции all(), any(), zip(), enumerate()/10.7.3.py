abscissas = map(lambda x: float(x), input().split())
ordinates = map(lambda x: float(x), input().split())
applicates = map(lambda x: float(x), input().split())

ans = []
for ab, o, ap in zip(abscissas, ordinates, applicates):
    if ab ** 2 + o ** 2 + ap ** 2 <= 4:
        ans.append(True)
    else:
        ans.append(False)
        break 

print(all(ans))