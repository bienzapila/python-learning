from functools import reduce

ans = []
for _ in range(int(input())):
    s = input()
    ans.append([s, reduce(lambda y, z: y + z, [int(x) for x in s.split('.')], 0)])

ans = sorted(ans, key=lambda x: x[1])
print(*list(ans)) 