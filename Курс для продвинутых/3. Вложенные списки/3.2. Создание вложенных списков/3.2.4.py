s = int(input())
# создаем первые два элемента, т. к. логика к ним не применима
sp = [[1], [1, 1]]

# заполняем последующие элементы
for i in range(2, s + 1):
    # половина строки
    spi = []
    spi.append(1)
    for k in range(1, i // 2 + 1):
        spi.append(sp[i - 1][k - 1] + sp[i - 1][k])
    spitrue = spi
    spi = spi[::-1]
    spika = spitrue + spi
    sp.append(spika)
for i in range(len(sp)):
    if i % 2 == 0:
        del sp[i][len(sp[i]) // 2]
sp[0] = [1]
for s in sp[:-1]:
    print(*s)
