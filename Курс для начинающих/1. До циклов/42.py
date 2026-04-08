n = int(input())
ma =  0
ma2 = 0
for i in range (1, n+1):
    num = int(input())
    if num >= ma:
        ma2 = ma
        ma = num
    if ma2 < num < ma:
        ma2 = num
print(ma, ma2, sep='\n')