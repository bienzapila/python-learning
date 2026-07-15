numbers = [5, 46, 47, 8, 12, 95, 32]

ans = map(lambda x: x // 2 if x % 2 == 0 else x, filter(lambda x: x < 48 if x % 2 == 1 else True, numbers))
print(*ans)