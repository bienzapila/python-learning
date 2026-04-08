a = int(input())
a1 = a // 100
a3 = a % 10
a2 = a % 100 // 10
if max(a1, a2, a3) - min(a1, a2, a3) == a1+a2+a3 - min(a1,a2,a3)-max(a1,a2,a3):
    print("Число интересное")
else:
    print('Число неинтересное')