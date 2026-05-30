def matrix(n=1, m=None, value=0):
    if n != 1 and m == None:
        m = n
    elif n == 1 and m == None:
        m = 1
    return [[value] * m for _ in range(n)]


from pprint import pprint

pprint(matrix(3, 1))
