tuples = [(1, 2), (), (3,), ()]
new = []
for i in range(len(tuples)):
    tuples[i] = list(tuples[i])
    tuples[i][-1] = 100
    tuples[i] = tuple(tuples[i])

print(tuples)
