data = input().split()
print(*list(sorted(data, key=lambda x: x.lower())))