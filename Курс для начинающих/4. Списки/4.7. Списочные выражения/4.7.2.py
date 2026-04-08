s = input()
sp = s.split()

spa = [int(num) ** 3 for num in sp]
print(*spa)
