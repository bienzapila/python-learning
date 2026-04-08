def solve(a, b, c):
    from math import sqrt

    D = b**2 - 4 * a * c
    if D == 0:
        return -b / (2 * a), -b / (2 * a)
    if D > 0:
        return min((-b - sqrt(D)) / (2 * a), (-b + sqrt(D)) / (2 * a)), max(
            (-b - sqrt(D)) / (2 * a), (-b + sqrt(D)) / (2 * a)
        )


a, b, c = int(input()), int(input()), int(input())
