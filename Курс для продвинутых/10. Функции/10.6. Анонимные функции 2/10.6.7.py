data = [
    (19542209, 'New York'), (4887871, 'Alabama'),
    (1420491, 'Hawaii'), (626299, 'Vermont'),
    (1805832, 'West Virginia'), (39865590, 'California'),
]

ans = sorted(data, key=lambda x: x[1][-1], reverse=True)

for a in ans:
    print(f'{a[1]}: {a[0]}')