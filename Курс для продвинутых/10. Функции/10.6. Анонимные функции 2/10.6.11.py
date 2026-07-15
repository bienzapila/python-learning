rgb = [int(s) for s in input().split()]

print(*(map(lambda x: 255 - x, rgb)))