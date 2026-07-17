from functools import reduce

ans = [input() for _ in range(int(input()))]
gem = [reduce(lambda y, z: y + ord(z) - ord('A'), x.upper(), 0) for x in ans]
final = sorted(zip(gem, ans))

for s in final:
    print(s[1])