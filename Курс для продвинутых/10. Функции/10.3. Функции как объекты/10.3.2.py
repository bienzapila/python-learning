points = [(3, 4), (-2, 1), (0, 1), (5, 12)]

def comparator(point):
    return (point[0] ** 2 + point[1] ** 2) ** (1/2)

print(sorted(points, key=comparator))