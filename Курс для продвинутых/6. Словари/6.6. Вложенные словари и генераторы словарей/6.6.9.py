tuples = [(26, 1, 30), (47, 5, 4), (11, 7, 9)]
final = {tuples[i][0]: tuples[i][1:] for i in range(len(tuples))}
print(final)
