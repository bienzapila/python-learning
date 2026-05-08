colors = {"a1": "Blue", "b2": "Orange", "b4": None, "a6": "Red", "c4": None}
ans = {c: colors[c] for c in colors if colors[c] != None}
print(ans)
