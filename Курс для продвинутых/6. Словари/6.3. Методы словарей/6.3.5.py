text = "TheyDon'tKnowThatWeKnowTheyKnowWeKnow"
d = {}
for s in text:
    if s in d:
        continue
    else:
        d[s] = text.count(s)

print(d)
