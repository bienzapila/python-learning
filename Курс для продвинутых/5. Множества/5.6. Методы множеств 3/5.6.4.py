s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())

ans = s1 | s2 | s3
ans -= s1 & s2 & s3
print(*sorted(list(ans), key=int))
