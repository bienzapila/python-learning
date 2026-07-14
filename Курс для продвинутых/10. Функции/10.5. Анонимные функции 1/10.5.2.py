from functools import reduce

data = [
    ['Bangkok', 18180280, 'admin'], ['Karachi', 21422590, 'primary'],
    ['Bengaluru', 13187098, 'primary'],
]

print(reduce(lambda x, y: x + y, map(lambda x: " " + x[0] + ',', filter(lambda x: x[2] == 'primary' and x[1] > 10000000, sorted(data))), 'Cities:')[:-1])