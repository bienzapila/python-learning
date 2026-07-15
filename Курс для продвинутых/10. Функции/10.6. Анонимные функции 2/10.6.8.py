data = ['город', 'село', 'молоко', 'небо', 'сад']

ans = sorted(sorted(data), key=lambda x: len(x))

print(*ans)