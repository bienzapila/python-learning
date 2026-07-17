def pretty_print(data, side='-', delimiter='|'):
    l = 3 * len(data) + 1
    s = f'{delimiter}'
    for n in data:
        l += len(str(n))
        s += f' {n} {delimiter}'

    print(f'''{side * l}
{s}
{side * l}
''')

pretty_print([1, 2, 3, 4, 5])
pretty_print(
    ['10', '21', '311', '434', '5432'],
)
pretty_print(
    [10, 78, 564, 123456], side='^',
)
pretty_print(
    ['10', '78', '564', '123456'],
    delimiter='!',
)
pretty_print(
    [10, 78, 564, 123456],
    side='*',
    delimiter='!',
)