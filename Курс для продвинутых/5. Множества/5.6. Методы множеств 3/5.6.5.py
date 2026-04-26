s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())

print(*sorted(list(s3 - s1 - s2), reverse=True, key=int))
